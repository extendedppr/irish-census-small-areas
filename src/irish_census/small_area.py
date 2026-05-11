import os
import statistics

import ijson
from pyproj import Geod
from shapely.geometry import shape
from cached_property import cached_property

from irish_census.settings import (
    SMALL_AREA_NATIONAL_STATISTICAL_BOUNDARIES_2022,
    SMALL_AREA_NATIONAL_STATISTICAL_BOUNDARIES_2022_WITH_PROPERTIES,
    CONFIG_MAP,
)
from irish_census.utils import haversine, compute_bbox
from irish_census.demographics import Demographics, aggregate_demographics
from irish_census.marital_status import MaritalStatus, aggregate_marital_status
from irish_census.households import Households, aggregate_households
from irish_census.social import Social, aggregate_social
from irish_census.occupation import Occupation, aggregate_occupation
from irish_census.migration import Migration, aggregate_migrations
from irish_census.ethnic import Ethnicity, aggregate_ethnicities
from irish_census.religion import Religion, aggregate_religion
from irish_census.housing_type import HousingType, aggregate_housing_types
from irish_census.housing_built_year import (
    HousingBuiltYear,
    aggregate_housing_built_year,
)
from irish_census.type_of_occupancy import TypeOfOccupancy, aggregate_type_of_occupancy


class SmallArea:
    def __init__(self, *args, **kwargs):
        self.object_id = kwargs["object_id"]
        self._shape = kwargs["shape"]
        self.county = kwargs["county"]
        self.place_name = kwargs["place_name"]

        self.population = kwargs["population"]
        self.marital_status = kwargs["marital_status"]
        self.households = kwargs["households"]
        self.social = kwargs["social"]
        self.occupation = kwargs["occupation"]
        self.migration = kwargs["migration"]
        self.ethnicities = kwargs["ethnicities"]
        self.religion = kwargs["religion"]
        self.housing_type = kwargs["housing_type"]
        self.year_built = kwargs["year_built"]
        self.type_of_occupancy = kwargs["type_of_occupancy"]

    @staticmethod
    def parse(geojson_feature):
        def build_kwarg(model, key):
            data = properties.get(key)
            return model(data) if data else None

        for k, v in CONFIG_MAP.items():
            if not geojson_feature["properties"].get(v["data_key"]):
                print(
                    f"No {k} for OBJECTID {geojson_feature['properties']['OBJECTID']} Results may be incorrect, consider downloading"
                )

        properties = geojson_feature["properties"]

        return SmallArea(
            object_id=properties["OBJECTID"],
            shape=geojson_feature["geometry"],
            county=properties["COUNTY_ENGLISH"],
            place_name=properties["ED_ENGLISH"],
            population=build_kwarg(
                Demographics, CONFIG_MAP["population_demos"]["data_key"]
            ),
            marital_status=build_kwarg(
                MaritalStatus, CONFIG_MAP["marital_status"]["data_key"]
            ),
            households=build_kwarg(Households, CONFIG_MAP["households"]["data_key"]),
            social=build_kwarg(Social, CONFIG_MAP["social"]["data_key"]),
            occupation=build_kwarg(Occupation, CONFIG_MAP["occupations"]["data_key"]),
            migration=build_kwarg(Migration, CONFIG_MAP["migration"]["data_key"]),
            ethnicities=build_kwarg(Ethnicity, CONFIG_MAP["ethnicities"]["data_key"]),
            religion=build_kwarg(Religion, CONFIG_MAP["religion"]["data_key"]),
            housing_type=build_kwarg(
                HousingType, CONFIG_MAP["housing_type"]["data_key"]
            ),
            year_built=build_kwarg(
                HousingBuiltYear, CONFIG_MAP["housing_built_year"]["data_key"]
            ),
            type_of_occupancy=build_kwarg(
                TypeOfOccupancy, CONFIG_MAP["type_of_occupancy"]["data_key"]
            ),
        )

    def distance_from(self, lat, lng, search_radius=None):
        # Skips fast processing for multi poly since there's not many

        if search_radius and self._shape["type"] == "Polygon":
            # very loose with 5 times the search radius
            radius_pad = (search_radius * 5) / 111
            distance_pad = 15 / 111

            pad = max([radius_pad, distance_pad])

            bbox = compute_bbox(self._shape["coordinates"][0])

            min_lng, min_lat, max_lng, max_lat = bbox

            if (
                lat < min_lat - pad
                or lat > max_lat + pad
                or lng < min_lng - pad
                or lng > max_lng + pad
            ):
                return float("inf")

        centroid = self.shape.centroid
        return haversine(lat, lng, centroid.y, centroid.x)

    @property
    def area_km2(self):
        area, _ = Geod(ellps="WGS84").geometry_area_perimeter(self.shape)
        return abs(area) / 1e6

    @cached_property
    def shape(self):
        return shape(self._shape)

    def to_dict(self):
        return {
            "object_id": self.object_id,
            "shape": self.shape,
            "area": self.area_km2,
            "county": self.county,
            "place_name": self.place_name,
            "population": self.population.to_dict() if self.population else None,
            "marital_status": self.marital_status.to_dict()
            if self.marital_status
            else None,
            "households": self.households.to_dict() if self.households else None,
            "social": self.social.to_dict() if self.social else None,
            "occupation": self.occupation.to_dict() if self.occupation else None,
            "migration": self.migration.to_dict() if self.migration else None,
            "ethnicities": self.ethnicities.to_dict() if self.ethnicities else None,
            "religion": self.religion.to_dict() if self.religion else None,
            "housing_type": self.housing_type.to_dict() if self.housing_type else None,
            "year_built": self.year_built.to_dict() if self.year_built else None,
            "type_of_occupancy": self.type_of_occupancy.to_dict()
            if self.type_of_occupancy
            else None,
        }


class SmallAreas:
    def __init__(self, geojson=None):
        if geojson is None:
            print("Loading geojson")

            geojson_fp = (
                SMALL_AREA_NATIONAL_STATISTICAL_BOUNDARIES_2022_WITH_PROPERTIES
                if os.path.exists(
                    SMALL_AREA_NATIONAL_STATISTICAL_BOUNDARIES_2022_WITH_PROPERTIES
                )
                else SMALL_AREA_NATIONAL_STATISTICAL_BOUNDARIES_2022
            )

            self._data = []
            with open(geojson_fp, "rb") as f:
                for feature in ijson.items(f, "features.item", use_float=True):
                    self._data.append(SmallArea.parse(feature))

            print("Loaded geojson")
        else:
            self._data = [SmallArea.parse(f) for f in geojson["features"]]

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        return iter(self._data)

    def __getitem__(self, idx):
        return self._data[idx]

    def append(self, area):
        assert isinstance(area, SmallArea)
        self._data.append(area)

    def get_around_point(self, lat, lng, radius_km):
        """
        Given a lat/lng and radius_km get stats of the small areas
        where the centre point is within the radius
        """
        result = SmallAreas(geojson={"type": "FeatureCollection", "features": []})

        for area in self:
            if area.distance_from(lat, lng, search_radius=radius_km) < radius_km:
                result.append(area)

        return result

    def to_dict(self):
        def collect(attr):
            return [getattr(sa, attr) for sa in self if getattr(sa, attr)]

        populations = collect("population")
        marital_status = collect("marital_status")
        households = collect("households")
        social = collect("social")
        occupation = collect("occupation")
        migrations = collect("migration")
        ethnicities = collect("ethnicities")
        religions = collect("religion")
        housing_types = collect("housing_type")
        year_built = collect("year_built")
        type_of_occupancy = collect("type_of_occupancy")

        total_population = sum(
            [population.total_population for population in populations]
        )
        area = sum([small_area.area_km2 for small_area in self])

        return {
            "number_of_zones": len(self),
            "area_km2": area,
            "population_density": total_population / area,
            "total_population": total_population,
            "approx_mean_age": statistics.mean([p.approx_mean_age for p in populations])
            if populations
            else None,
            "population": aggregate_demographics(populations),
            "marital_status": aggregate_marital_status(marital_status),
            "households": aggregate_households(households),
            "social": aggregate_social(social),
            "occupation": aggregate_occupation(occupation),
            "migration": aggregate_migrations(migrations),
            "ethnicity": aggregate_ethnicities(ethnicities),
            "religion": aggregate_religion(religions),
            "housing_type": aggregate_housing_types(housing_types),
            "housing_built_year": aggregate_housing_built_year(year_built),
            "type_of_occupancy": aggregate_type_of_occupancy(type_of_occupancy),
        }

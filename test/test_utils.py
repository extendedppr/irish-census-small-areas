import os
import json

from unittest import TestCase

from irish_census.utils import (
    haversine,
    compute_bbox,
    clean_string_to_snake,
    aggregate,
    parse_gender,
    parse,
    convert_geojson_29903_to_4326,
)
from irish_census.demographics import Demographics


class UtilsTest(TestCase):
    BASE_RESOURCES = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "test/resources/",
    )

    POPULATION_DATA_FILE_PATH = os.path.join(
        BASE_RESOURCES, "downloads/population/000581a3-4ebd-4a74-b5f8-0bd78cd7ede5.json"
    )

    SAMPLE_DEMOGRAPHICS = Demographics(
        json.loads(open(POPULATION_DATA_FILE_PATH, "r").read())
    )

    def test_haversine(self):
        self.assertEqual(round(haversine(0, 0, 1, 1), 2), 157.25)

    def test_compute_bbox(self):
        self.assertEqual(
            compute_bbox(
                [
                    [0, 0],
                    [0, 1],
                    [1, 1],
                    [1, 0],
                    [0, 0],
                ]
            ),
            (0, 0, 1, 1),
        )

    def test_clean_string_to_snake(self):
        self.assertEqual(clean_string_to_snake("abc def gh_ijk"), "abc_def_gh_ijk")

    def test_aggregate(self):
        self.assertEqual(
            aggregate(["male", "female"], [self.SAMPLE_DEMOGRAPHICS])["male"][
                "age_0-4"
            ],
            14,
        )

    def test_parse_gender(self):
        self.assertEqual(
            parse_gender(
                json.loads(open(self.POPULATION_DATA_FILE_PATH, "r").read()),
                "C03737V04485",
                reverse=False,
            )["male"]["age_0-4"],
            14,
        )

    def test_convert_geojson_29903_to_4326(self):
        geojson = {
            "type": "FeatureCollection",
            "features": [
                {
                    "type": "Feature",
                    "properties": {"name": "test"},
                    "geometry": {
                        "type": "Point",
                        "coordinates": [0.0, 0.0],
                    },
                }
            ],
        }

        self.assertEqual(
            convert_geojson_29903_to_4326(geojson)["features"][0]["geometry"][
                "coordinates"
            ],
            [-15.817314303458238, 46.488181433431954],
        )

    def test_parse(self):
        # Doesn't make sense to do this but is enough to test the function
        self.assertEqual(
            parse(
                json.loads(open(self.POPULATION_DATA_FILE_PATH, "r").read()),
                "C03737V04485",
            )["population"]["age_0-4"],
            14,
        )

import sys
import os


TEST_ENV = False
if "pytest" in sys.modules:
    TEST_ENV = True

LOG_LOCATION = (
    "/var/log/irish_census/irish_census.log"
    if not TEST_ENV
    else "/tmp/log/irish_census/irish_census.log"
)

DATA_LOCATION = (
    os.getenv("IRISH_CENSUS_DATA_LOCATION", "/var/lib/irish_census")
    if not TEST_ENV
    else "/tmp/var/lib/irish_census/"
)


DOWNLOADS_LOCATION = os.path.join(DATA_LOCATION, "downloads")
POPULATION_LOCATION = os.path.join(DOWNLOADS_LOCATION, "population")
MARITAL_LOCATION = os.path.join(DOWNLOADS_LOCATION, "marital")
PRIVATE_HOUSEHOLDS_LOCATION = os.path.join(DOWNLOADS_LOCATION, "private_households")
SOCIAL_LOCATION = os.path.join(DOWNLOADS_LOCATION, "social")
OCCUPATION_LOCATION = os.path.join(DOWNLOADS_LOCATION, "occupations")
MIGRATION_LOCATION = os.path.join(DOWNLOADS_LOCATION, "migration")
ETHNICITY_LOCATION = os.path.join(DOWNLOADS_LOCATION, "ethnicity")
RELIGION_LOCATION = os.path.join(DOWNLOADS_LOCATION, "religion")
HOUSING_TYPE_LOCATION = os.path.join(DOWNLOADS_LOCATION, "housing_type")
HOUSING_BUILT_YEAR_LOCATION = os.path.join(DOWNLOADS_LOCATION, "housing_built_year")
TYPE_OF_OCCUPANCY_LOCATION = os.path.join(DOWNLOADS_LOCATION, "type_of_occupancy")
PRIVATE_HOUSEHOLDS_BY_NUMBER_OF_ROOMS = os.path.join(
    DOWNLOADS_LOCATION, "private_households_by_number_of_rooms"
)

SMALL_AREA_NATIONAL_STATISTICAL_BOUNDARIES_2022 = os.path.join(
    DOWNLOADS_LOCATION,
    "Small_Area_National_Statistical_Boundaries_2022.geojson",
)
SMALL_AREA_NATIONAL_STATISTICAL_BOUNDARIES_2022_WITH_PROPERTIES = os.path.join(
    DATA_LOCATION,
    "Small_Area_National_Statistical_Boundaries_2022_With_Properties.geojson",
)


CONFIG_MAP = {
    "population_demos": {
        "dir": POPULATION_LOCATION,
        "matrix": "SAP2022T1T1ASA",
        "data_key": "population_data",
    },
    "ethnicities": {
        "dir": ETHNICITY_LOCATION,
        "matrix": "SAP2022T2T2SA",
        "pivot": None,
        "data_key": "ethnicities_data",
    },
    "migration": {
        "dir": MIGRATION_LOCATION,
        "matrix": "SAP2022T2T1SA",
        "data_key": "migration_data",
    },
    "occupations": {
        "dir": OCCUPATION_LOCATION,
        "matrix": "SAP2022T13T1SA",
        "pivot": "C03738V04487",
        "data_key": "occupation_data",
    },
    "social": {
        "dir": SOCIAL_LOCATION,
        "matrix": "SAP2022T9T1SA",
        "pivot": "C03738V04487",
        "data_key": "social_data",
    },
    "households": {
        "dir": PRIVATE_HOUSEHOLDS_LOCATION,
        "matrix": "SAP2022T5T1SA",
        "data_key": "households_data",
    },
    "religion": {
        "dir": RELIGION_LOCATION,
        "matrix": "SAP2022T2T4SA",
        "data_key": "religion_data",
    },
    "marital_status": {
        "dir": MARITAL_LOCATION,
        "matrix": "SAP2022T1T2SA",
        "data_key": "marital_status_data",
    },
    "housing_type": {
        "dir": HOUSING_TYPE_LOCATION,
        "matrix": "SAP2022T6T1SA",
        "data_key": "housing_type_data",
    },
    "housing_built_year": {
        "dir": HOUSING_BUILT_YEAR_LOCATION,
        "matrix": "SAP2022T6T2SA",
        "data_key": "housing_built_year_data",
    },
    "type_of_occupancy": {
        "dir": TYPE_OF_OCCUPANCY_LOCATION,
        "matrix": "SAP2022T6T3SA",
        "data_key": "type_of_occupancy_data",
    },
    "private_households_by_number_of_rooms": {
        "dir": PRIVATE_HOUSEHOLDS_BY_NUMBER_OF_ROOMS,
        "matrix": "SAP2022T6T4SA",
        "data_key": "private_households_by_number_of_rooms",
    },
}

os.makedirs(DATA_LOCATION, exist_ok=True)
for k, v in CONFIG_MAP.items():
    os.makedirs(v["dir"], exist_ok=True)

import os
import json
from decimal import Decimal

import ijson
import orjson
import progressbar

from irish_census.settings import (
    SMALL_AREA_NATIONAL_STATISTICAL_BOUNDARIES_2022,
    SMALL_AREA_NATIONAL_STATISTICAL_BOUNDARIES_2022_WITH_PROPERTIES,
    CONFIG_MAP,
)


def convert(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    raise obj


def set_data(loc, prop, feature):
    guid = feature["properties"]["SA_GUID_2022"]
    fp = os.path.join(loc, f"{guid}.json")

    if not os.path.exists(fp):
        print(f"No local file: {fp}")
        feature["properties"][prop] = None
        return

    try:
        with open(fp, "rb") as f:
            feature["properties"][prop] = orjson.loads(f.read())
    except orjson.JSONDecodeError:
        print(f"Error decoding JSON: {fp}")
        feature["properties"][prop] = None


def merge(features_count=None):
    # Pretty ugly as so much memory is used otherwise
    with (
        open(SMALL_AREA_NATIONAL_STATISTICAL_BOUNDARIES_2022, "rb") as src,
        open(
            SMALL_AREA_NATIONAL_STATISTICAL_BOUNDARIES_2022_WITH_PROPERTIES, "wb"
        ) as out,
    ):
        out.write(b'{"type":"FeatureCollection","features":[')

        first = True

        features = ijson.items(src, "features.item")

        for feature in progressbar.progressbar(features, max_value=features_count):
            for _, config in CONFIG_MAP.items():
                set_data(config["dir"], config["data_key"], feature)

            if not first:
                out.write(b",")

            out.write(json.dumps(feature, default=convert).encode())
            first = False

        out.write(b"]}")

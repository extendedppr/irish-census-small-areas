import os
import argparse
import requests
from time import sleep
from pathlib import Path

import orjson
import progressbar

from irish_census.settings import (
    SMALL_AREA_NATIONAL_STATISTICAL_BOUNDARIES_2022,
    CONFIG_MAP,
)
from irish_census.downloader import small_area_download_guid
from irish_census.merger import merge
from irish_census.utils import convert_geojson_29903_to_4326


def download(small_areas, loc, config):
    for feature in progressbar.progressbar(small_areas["features"]):
        if small_area_download_guid(
            feature["properties"]["SA_GUID_2022"],
            config["dir"],
            matrix=config["matrix"],
            pivot=config.get("pivot"),
        ):
            sleep(0.5)


def download_small_areas():
    if not os.path.exists(SMALL_AREA_NATIONAL_STATISTICAL_BOUNDARIES_2022):
        print("Downloading general boundaries")

        url = "https://data-osi.opendata.arcgis.com/api/download/v1/items/70a33cbb8bd7406da0d571be28624721/geojson?layers=0"
        output_path = Path(SMALL_AREA_NATIONAL_STATISTICAL_BOUNDARIES_2022)

        response = requests.get(url, stream=True, timeout=60)
        response.raise_for_status()

        with open(output_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)

        with open(SMALL_AREA_NATIONAL_STATISTICAL_BOUNDARIES_2022) as f:
            data = orjson.loads(f.read())

        converted = convert_geojson_29903_to_4326(data)

        with open(SMALL_AREA_NATIONAL_STATISTICAL_BOUNDARIES_2022, "w") as f:
            orjson.dump(converted, f)


def main():
    parser = argparse.ArgumentParser(description="Download census data")
    parser.add_argument(
        "--type",
        choices=list(CONFIG_MAP.keys()),
        required=False,
    )

    args = parser.parse_args()

    download_small_areas()

    small_areas = None
    with open(
        SMALL_AREA_NATIONAL_STATISTICAL_BOUNDARIES_2022,
        "r",
    ) as f:
        try:
            small_areas = orjson.loads(f.read())
        except orjson.JSONDecodeError:
            raise Exception("Bad json file, delete and download again")

    if not args.type:
        for k, v in CONFIG_MAP.items():
            print(f"Downloading: {k}")
            download(small_areas, k, v)
    else:
        download(small_areas, args.type, CONFIG_MAP[args.type])

    print("Merge data")
    merge(features_count=len(small_areas["features"]))


if __name__ == "__main__":
    main()

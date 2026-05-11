import json
import os

import requests


def small_area_download_guid(guid, dir_location, matrix=None, pivot=None):
    fp = os.path.join(dir_location, f"{guid}.json")

    if os.path.exists(fp) and os.path.getsize(fp) == 0:
        print(f"Bad file, replacing: {fp}")
        os.remove(fp)

    if os.path.exists(fp):
        return False

    payload = {
        "jsonrpc": "2.0",
        "method": "PxStat.Data.Cube_API.ReadDataset",
        "params": {
            "class": "query",
            "id": ["C04172V04943"],
            "dimension": {"C04172V04943": {"category": {"index": [guid]}}},
            "extension": {
                "pivot": pivot,
                "codes": False,
                "language": {"code": "en"},
                "format": {"type": "JSON-stat", "version": "2.0"},
                "matrix": matrix,
            },
            "version": "2.0",
            "m2m": False,
        },
        "id": "dl",
    }

    response = requests.post(
        "https://ws.cso.ie/public/api.jsonrpc", headers={}, json=payload, timeout=30
    )
    response.raise_for_status()

    data = response.json()

    with open(fp, "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False)

    return True

import math
from collections import defaultdict

from pyproj import Transformer


def haversine(lat1, lon1, lat2, lon2):
    R = 6371
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)

    a = (
        math.sin(dphi / 2) ** 2
        + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2) ** 2
    )
    return 2 * R * math.atan2(math.sqrt(a), math.sqrt(1 - a))


def compute_bbox(coords):
    lngs = [p[0] for p in coords]
    lats = [p[1] for p in coords]
    return min(lngs), min(lats), max(lngs), max(lats)


def clean_string_to_snake(s):
    return s.lower().replace(" ", "_")


def aggregate(total_keys, data_list):
    totals = {k: defaultdict(int) for k in total_keys}

    for item in data_list:
        for total in totals.keys():
            for k, v in item.data[total].items():
                if k == "total":
                    continue
                if not v:
                    v = 0
                totals[total][k] += v

    for total in totals.keys():
        totals[total] = dict(totals[total])

    return totals


def parse_gender(payload, dim, reverse=True):
    result = payload["result"]
    values = result["value"]
    dims = result["dimension"]

    classes = dims[dim]["category"]["label"]

    data = defaultdict(lambda: defaultdict(int))

    genders = ["male", "female", "both"]

    outer_loop = genders if reverse else classes.items()
    inner_loop = classes.items() if reverse else genders

    i = 0
    for outer in outer_loop:
        for inner in inner_loop:
            gender = outer if reverse else inner
            class_label = inner[1] if reverse else outer[1]
            class_name = clean_string_to_snake(class_label)

            if class_name != "total":
                data[gender][class_name] = values[i]

            i += 1

    return {gender: dict(values) for gender, values in data.items()}


def parse(payload, dim):
    result = payload["result"]
    values = result["value"]

    stats = result["dimension"]["STATISTIC"]["category"]["index"]
    stat_labels = result["dimension"]["STATISTIC"]["category"]["label"]

    migrations = result["dimension"][dim]["category"]["index"]
    migration_labels = result["dimension"][dim]["category"]["label"]

    data = {}
    idx = 0
    for stat in stats:
        stat_name = clean_string_to_snake(stat_labels[stat])
        data[stat_name] = {}

        for migration in migrations:
            migration_name = clean_string_to_snake(migration_labels[migration])
            data[stat_name][migration_name] = values[idx]
            idx += 1

    return data


def convert_geojson_29903_to_4326(data):
    transformer = Transformer.from_crs("EPSG:2157", "EPSG:4326", always_xy=True)

    def transform_coords(coords):
        if isinstance(coords[0], (int, float)):
            lon, lat = transformer.transform(coords[0], coords[1])
            return [lon, lat]
        return [transform_coords(c) for c in coords]

    def process(obj):
        if obj["type"] == "FeatureCollection":
            obj["features"] = [process(f) for f in obj["features"]]
        elif obj["type"] == "Feature":
            obj["geometry"] = process(obj["geometry"])
        elif "coordinates" in obj:
            obj["coordinates"] = transform_coords(obj["coordinates"])
        return obj

    return process(data)

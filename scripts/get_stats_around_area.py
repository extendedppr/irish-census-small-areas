import argparse


from irish_census.small_area import SmallAreas


def main():
    parser = argparse.ArgumentParser(description="Get all stats around a point")
    parser.add_argument(
        "--lat",
        type=float,
        required=True,
    )
    parser.add_argument(
        "--lng",
        type=float,
        required=True,
    )
    parser.add_argument("--radius-km", type=float, required=True, default=5.0)

    args = parser.parse_args()

    small_areas = SmallAreas().get_around_point(args.lat, args.lng, args.radius_km)

    import pprint

    pprint.pprint(small_areas.to_dict())


if __name__ == "__main__":
    main()

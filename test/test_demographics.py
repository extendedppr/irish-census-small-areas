import os
import json

from unittest import TestCase

from irish_census.demographics import Demographics, aggregate_demographics


class DemographicsTest(TestCase):
    BASE_RESOURCES = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "test/resources/",
    )

    DATA_FILE_PATH = os.path.join(
        BASE_RESOURCES, "downloads/population/000581a3-4ebd-4a74-b5f8-0bd78cd7ede5.json"
    )

    SAMPLE_DEMOGRAPHICS = Demographics(json.loads(open(DATA_FILE_PATH, "r").read()))

    def test_total_population(self):
        self.assertEqual(self.SAMPLE_DEMOGRAPHICS.total_population, 260)

    def test_approx_mean_age(self):
        self.assertEqual(round(self.SAMPLE_DEMOGRAPHICS.approx_mean_age), 30)

    def test_aggregate_demographics(self):
        self.assertEqual(
            aggregate_demographics([self.SAMPLE_DEMOGRAPHICS])["male"]["age_0-4"], 14
        )
        self.assertEqual(
            aggregate_demographics(
                [self.SAMPLE_DEMOGRAPHICS, self.SAMPLE_DEMOGRAPHICS]
            )["male"]["age_0-4"],
            28,
        )

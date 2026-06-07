import os
import json

from unittest import TestCase

from irish_census.marital_status import MaritalStatus


class MaritalStatusTest(TestCase):
    BASE_RESOURCES = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "test/resources/",
    )

    DATA_FILE_PATH = os.path.join(
        BASE_RESOURCES,
        "downloads/marital_status/000581a3-4ebd-4a74-b5f8-0bd78cd7ede5.json",
    )

    SAMPLE_MARITAL_STATUS = MaritalStatus(json.loads(open(DATA_FILE_PATH, "r").read()))

    def test_parse(self):
        self.assertEqual(
            self.SAMPLE_MARITAL_STATUS.__dict__,
            {
                "model_name": "MaritalStatus",
                "data": {
                    "male": {
                        "single": 62.0,
                        "married": 48.0,
                        "separated": 1.0,
                        "divorced": 1.0,
                        "widowed": 0.0,
                    },
                    "female": {
                        "single": 83.0,
                        "married": 52.0,
                        "separated": 3.0,
                        "divorced": 3.0,
                        "widowed": 7.0,
                    },
                    "both": {
                        "single": 145.0,
                        "married": 100.0,
                        "separated": 4.0,
                        "divorced": 4.0,
                        "widowed": 7.0,
                    },
                },
            },
        )

from unittest import TestCase

from irish_census.utils import haversine, compute_bbox


class UtilsTest(TestCase):
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

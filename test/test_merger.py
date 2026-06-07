from decimal import Decimal

from unittest import TestCase

from irish_census.merger import convert


class MergerTest(TestCase):
    def test_convert(self):
        self.assertEqual(convert(Decimal(1.5)), 1.5)
        self.assertEqual(convert(1.5), 1.5)

from unittest import TestCase

from irish_census.downloader import create_payload


class DownloaderTest(TestCase):
    def test_create_payload(self):
        self.assertEqual(
            create_payload("guidguid", matrix="123", pivot="456"),
            {
                "jsonrpc": "2.0",
                "method": "PxStat.Data.Cube_API.ReadDataset",
                "params": {
                    "class": "query",
                    "id": ["C04172V04943"],
                    "dimension": {
                        "C04172V04943": {"category": {"index": ["guidguid"]}}
                    },
                    "extension": {
                        "pivot": "456",
                        "codes": False,
                        "language": {"code": "en"},
                        "format": {"type": "JSON-stat", "version": "2.0"},
                        "matrix": "123",
                    },
                    "version": "2.0",
                    "m2m": False,
                },
                "id": "dl",
            },
        )

from unittest import TestCase

from irish_census.small_area import SmallArea, SmallAreas


SAMPLE_GEOJSON_FEATURE = {
    "type": "Feature",
    "id": 13949,
    "geometry": {
        "type": "Polygon",
        "coordinates": [
            [
                [-8.83989022873269, 53.5081501964028],
                [-8.83993514774769, 53.508128527779],
                [-8.84008918313975, 53.508054219626],
                [-8.84011126926838, 53.5080435676415],
                [-8.84013824224391, 53.5080337979794],
                [-8.84138635012205, 53.5075817289208],
                [-8.8427737659493, 53.5070791914245],
                [-8.84340676908328, 53.5068670292898],
                [-8.8435785380443, 53.5068094600129],
                [-8.84363751145178, 53.5067896948975],
                [-8.84367035263126, 53.5067786877511],
                [-8.84393062952063, 53.5080166745843],
                [-8.84400370380386, 53.5083112457203],
                [-8.84402389515139, 53.5083655246348],
                [-8.84397688664002, 53.5084107769709],
                [-8.84393070571818, 53.5084583834225],
                [-8.84383376197164, 53.5085529096554],
                [-8.84376565753927, 53.508613343311],
                [-8.84375366570202, 53.5086251559402],
                [-8.84373872791605, 53.5086396944371],
                [-8.84370742541876, 53.50867131582],
                [-8.84368519181549, 53.5086934907997],
                [-8.84364361813557, 53.5087347557712],
                [-8.84364012454076, 53.5087387526644],
                [-8.84361529419654, 53.508764540742],
                [-8.84359212308803, 53.5087896161223],
                [-8.84357960776153, 53.5088008842227],
                [-8.84355948870821, 53.5088209862417],
                [-8.8435307378565, 53.508849776651],
                [-8.84352428399688, 53.508855780548],
                [-8.84349853776176, 53.5088817637893],
                [-8.84347428459923, 53.508907017533],
                [-8.84345554794803, 53.5089253752958],
                [-8.84341809975209, 53.5089633577972],
                [-8.84337860698333, 53.5090031521035],
                [-8.84334588266958, 53.5090376781201],
                [-8.84329583905147, 53.5090874684383],
                [-8.84329084871403, 53.509092015097],
                [-8.84327628878688, 53.5091088964661],
                [-8.84324467342293, 53.5091399807123],
                [-8.84321167450511, 53.5091750379599],
                [-8.84319474292077, 53.509193203209],
                [-8.84316629742851, 53.5092199333588],
                [-8.84312299475537, 53.5092630077299],
                [-8.84308024340338, 53.509304999761],
                [-8.84303023224586, 53.5093556974182],
                [-8.8430135397457, 53.5093722433012],
                [-8.84298806146088, 53.5093973258424],
                [-8.84297751871367, 53.5094069713012],
                [-8.84295315624421, 53.5094290263469],
                [-8.84293504634714, 53.5094486018327],
                [-8.84291448251894, 53.5094660736949],
                [-8.8429023375393, 53.5094831087411],
                [-8.84288042971325, 53.5095164260017],
                [-8.84284696382124, 53.5095660453174],
                [-8.84281095365459, 53.5096210927124],
                [-8.84278033291275, 53.5096651110455],
                [-8.8427556397413, 53.5097054658372],
                [-8.84273587832654, 53.5097398364878],
                [-8.84270429104146, 53.5097921386064],
                [-8.84270134251792, 53.5097942857064],
                [-8.84235172618473, 53.5096059969187],
                [-8.84218419630612, 53.5095092993475],
                [-8.84211991484265, 53.5094721866789],
                [-8.84202139461858, 53.5094153182502],
                [-8.84131830008641, 53.5090094438046],
                [-8.84107100101669, 53.5088841972668],
                [-8.84089506575362, 53.5087950970943],
                [-8.840559194503, 53.5086300850847],
                [-8.84049990143456, 53.5085965573206],
                [-8.84040630379198, 53.5085436081184],
                [-8.84012164999978, 53.5083473367337],
                [-8.84000072476442, 53.5082443232645],
                [-8.83989022873269, 53.5081501964028],
            ]
        ],
    },
    "properties": {
        "OBJECTID": 13949,
        "SA_GUID_2016": "4c07d11e-3b1f-851d-e053-ca3ca8c0ca7f",
        "SA_GUID_2022": "4c07d11e-3b1f-851d-e053-ca3ca8c0ca7f",
        "SA_PUB2011": "067211024",
        "SA_PUB2016": "067211024",
        "SA_PUB2022": "067211024",
        "SA_GEOGID_2022": "A067211024",
        "SA_CHANGE_CODE": 0,
        "SA_URBAN_AREA_FLAG": 1,
        "SA_URBAN_AREA_NAME": "Tuam",
        "SA_NUTS1": "IE0",
        "SA_NUTS1_NAME": "Ireland",
        "SA_NUTS2": "IE04",
        "SA_NUTS2_NAME": "Northern and Western",
        "SA_NUTS3": "IE042",
        "SA_NUTS3_NAME": "West",
        "ED_GUID": "2ae19629-233e-13a3-e055-000000000001",
        "ED_OFFICIAL": "Y",
        "ED_ENGLISH": "TUAM RURAL",
        "ED_GAEILGE": "TUAIM (TUATH)",
        "ED_ID_STR": "067211",
        "ED_PART_COUNT": 1,
        "COUNTY_CODE": "27",
        "COUNTY_ENGLISH": "GALWAY",
        "COUNTY_GAEILGE": "Gaillimh",
        "CSO_LEA": "TUAM",
        "population_data": {
            "jsonrpc": "2.0",
            "result": {
                "class": "dataset",
                "dimension": {
                    "STATISTIC": {
                        "category": {
                            "index": ["SAP2022T1T1C01"],
                            "label": {"SAP2022T1T1C01": "Population"},
                            "unit": {
                                "SAP2022T1T1C01": {
                                    "decimals": 0,
                                    "label": "Number",
                                    "position": "end",
                                }
                            },
                        },
                        "label": "Statistic",
                    },
                    "TLIST(A1)": {
                        "category": {"index": ["2022"], "label": {"2022": "2022"}},
                        "label": "Census Year",
                    },
                    "C04172V04943": {
                        "category": {
                            "index": ["4c07d11e-3b1f-851d-e053-ca3ca8c0ca7f"],
                            "label": {
                                "4c07d11e-3b1f-851d-e053-ca3ca8c0ca7f": "067211024"
                            },
                        },
                        "label": "CSO Small Areas 2022",
                        "link": {
                            "enclosure": [
                                {
                                    "type": "application/geo+json",
                                    "href": "https://ws.cso.ie/public/api.static/PxStat.Data.GeoMap_API.Read/dc342ded3e0ec8884e99eebd766f8233",
                                }
                            ]
                        },
                    },
                    "C03737V04485": {
                        "category": {
                            "index": [
                                "AGE0-4",
                                "AGE5-9",
                                "AGE10-14",
                                "AGE15-19",
                                "AGE20-24",
                                "AGE25-29",
                                "AGE30-34",
                                "AGE35-39",
                                "AGE40-44",
                                "AGE45-49",
                                "AGE50-54",
                                "AGE55-59",
                                "AGE60-64",
                                "AGE65-69",
                                "AGE70-74",
                                "AGE75-79",
                                "AGE80-84",
                                "AGE85andover",
                                "AGET",
                            ],
                            "label": {
                                "AGE0-4": "Age 0-4",
                                "AGE5-9": "Age 5-9",
                                "AGE10-14": "Age 10-14",
                                "AGE15-19": "Age 15-19",
                                "AGE20-24": "Age 20-24",
                                "AGE25-29": "Age 25-29",
                                "AGE30-34": "Age 30-34",
                                "AGE35-39": "Age 35-39",
                                "AGE40-44": "Age 40-44",
                                "AGE45-49": "Age 45-49",
                                "AGE50-54": "Age 50-54",
                                "AGE55-59": "Age 55-59",
                                "AGE60-64": "Age 60-64",
                                "AGE65-69": "Age 65-69",
                                "AGE70-74": "Age 70-74",
                                "AGE75-79": "Age 75-79",
                                "AGE80-84": "Age 80-84",
                                "AGE85andover": "Age 85 and over",
                                "AGET": "Total",
                            },
                        },
                        "label": "Age",
                    },
                    "C03738V04487": {
                        "category": {
                            "index": ["M", "F", "B"],
                            "label": {"M": "Males", "F": "Females", "B": "Both Sexes"},
                        },
                        "label": "Sex",
                    },
                },
                "extension": {
                    "matrix": "SAP2022T1T1ASA",
                    "reasons": ["Planned release"],
                    "language": {"code": "en", "name": "English"},
                    "elimination": {
                        "C04172V04943": None,
                        "C03737V04485": "AGET",
                        "C03738V04487": "B",
                    },
                    "contact": {
                        "name": "",
                        "email": "census@cso.ie",
                        "phone": "(+353) 1 895 1460",
                    },
                    "subject": {"code": 88, "value": "SAPMAP 2022"},
                    "product": {
                        "code": "SM2022T1",
                        "value": "Theme 1: Sex, Age and Marital Status",
                    },
                    "official": True,
                    "copyright": {
                        "name": "Central Statistics Office, Ireland",
                        "code": "CSO",
                        "href": "https://www.cso.ie/",
                    },
                    "exceptional": False,
                    "reservation": False,
                    "archive": False,
                    "experimental": False,
                    "analytical": False,
                },
                "href": "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/SAP2022T1T1ASA/PX/2013/en",
                "id": [
                    "STATISTIC",
                    "TLIST(A1)",
                    "C04172V04943",
                    "C03737V04485",
                    "C03738V04487",
                ],
                "label": "Population",
                "link": {
                    "alternate": [
                        {
                            "type": "text/csv",
                            "href": "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/SAP2022T1T1ASA/CSV/1.0/en",
                        },
                        {
                            "type": "application/json",
                            "href": "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/SAP2022T1T1ASA/JSON-stat/2.0/en",
                        },
                        {
                            "type": "application/json",
                            "href": "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/SAP2022T1T1ASA/JSON-stat/1.0/en",
                        },
                        {
                            "type": "application/base64",
                            "href": "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/SAP2022T1T1ASA/XLSX/2007/en",
                        },
                    ]
                },
                "note": [
                    "",
                    "For more information, please go to the [url=https://www.cso.ie/en/statistics/population/censusofpopulation2022/]statistical release page[/url] on our website.",
                ],
                "role": {
                    "geo": ["C04172V04943"],
                    "metric": ["STATISTIC"],
                    "time": ["TLIST(A1)"],
                },
                "size": [1, 1, 1, 19, 3],
                "updated": "2023-09-15T11:00:00.000Z",
                "value": [
                    4.0,
                    10.0,
                    14.0,
                    9.0,
                    4.0,
                    13.0,
                    2.0,
                    7.0,
                    9.0,
                    6.0,
                    6.0,
                    12.0,
                    8.0,
                    13.0,
                    21.0,
                    6.0,
                    8.0,
                    14.0,
                    6.0,
                    7.0,
                    13.0,
                    9.0,
                    8.0,
                    17.0,
                    5.0,
                    3.0,
                    8.0,
                    5.0,
                    9.0,
                    14.0,
                    7.0,
                    9.0,
                    16.0,
                    6.0,
                    10.0,
                    16.0,
                    9.0,
                    12.0,
                    21.0,
                    5.0,
                    8.0,
                    13.0,
                    12.0,
                    13.0,
                    25.0,
                    5.0,
                    7.0,
                    12.0,
                    1.0,
                    4.0,
                    5.0,
                    4.0,
                    1.0,
                    5.0,
                    109.0,
                    139.0,
                    248.0,
                ],
                "version": "2.0",
            },
            "id": "285578803",
        },
    },
}


class SmallAreaTest(TestCase):
    def test_parse(self):
        area = SmallArea.parse(SAMPLE_GEOJSON_FEATURE)
        data = area.to_dict()
        self.assertEqual(data["object_id"], 13949)
        self.assertEqual(data["county"], "GALWAY")
        self.assertEqual(data["place_name"], "TUAM RURAL")
        self.assertEqual(
            data["population"],
            {
                "approx_mean_age": 43.542338709677416,
                "data": {
                    "male": {
                        "age_0-4": 4.0,
                        "age_5-9": 9.0,
                        "age_10-14": 2.0,
                        "age_15-19": 6.0,
                        "age_20-24": 8.0,
                        "age_25-29": 6.0,
                        "age_30-34": 6.0,
                        "age_35-39": 9.0,
                        "age_40-44": 5.0,
                        "age_45-49": 5.0,
                        "age_50-54": 7.0,
                        "age_55-59": 6.0,
                        "age_60-64": 9.0,
                        "age_65-69": 5.0,
                        "age_70-74": 12.0,
                        "age_75-79": 5.0,
                        "age_80-84": 1.0,
                        "age_85_and_over": 4.0,
                    },
                    "female": {
                        "age_0-4": 10.0,
                        "age_5-9": 4.0,
                        "age_10-14": 7.0,
                        "age_15-19": 6.0,
                        "age_20-24": 13.0,
                        "age_25-29": 8.0,
                        "age_30-34": 7.0,
                        "age_35-39": 8.0,
                        "age_40-44": 3.0,
                        "age_45-49": 9.0,
                        "age_50-54": 9.0,
                        "age_55-59": 10.0,
                        "age_60-64": 12.0,
                        "age_65-69": 8.0,
                        "age_70-74": 13.0,
                        "age_75-79": 7.0,
                        "age_80-84": 4.0,
                        "age_85_and_over": 1.0,
                    },
                    "both": {
                        "age_0-4": 14.0,
                        "age_5-9": 13.0,
                        "age_10-14": 9.0,
                        "age_15-19": 12.0,
                        "age_20-24": 21.0,
                        "age_25-29": 14.0,
                        "age_30-34": 13.0,
                        "age_35-39": 17.0,
                        "age_40-44": 8.0,
                        "age_45-49": 14.0,
                        "age_50-54": 16.0,
                        "age_55-59": 16.0,
                        "age_60-64": 21.0,
                        "age_65-69": 13.0,
                        "age_70-74": 25.0,
                        "age_75-79": 12.0,
                        "age_80-84": 5.0,
                        "age_85_and_over": 5.0,
                    },
                },
            },
        )

    def test_distance_from(self):
        geojson = {
            "type": "Feature",
            "id": 13949,
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [0, 0],
                        [1, 1],
                        [0, 0],
                    ]
                ],
            },
            "properties": {
                "OBJECTID": 1,
                "COUNTY_ENGLISH": "DUBLIN",
                "ED_ENGLISH": "DUBLIN SOMETHING",
            },
        }

        area = SmallArea.parse(geojson)
        self.assertEqual(round(area.distance_from(1, 1), 2), 78.62)

    def test_area(self):
        geojson = {
            "type": "Feature",
            "id": 13949,
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [0, 0],
                        [0, 1],
                        [1, 1],
                        [1, 0],
                        [0, 0],
                    ]
                ],
            },
            "properties": {
                "OBJECTID": 1,
                "COUNTY_ENGLISH": "DUBLIN",
                "ED_ENGLISH": "DUBLIN SOMETHING",
            },
        }

        area = SmallArea.parse(geojson)
        self.assertEqual(round(area.area_km2, 2), 12308.78)


class SmallAreasTest(TestCase):
    def test_get_around_point(self):
        geojson = {
            "type": "Feature",
            "id": 13949,
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [0, 0],
                        [1, 1],
                        [0, 0],
                    ]
                ],
            },
            "properties": {
                "OBJECTID": 1,
                "COUNTY_ENGLISH": "DUBLIN",
                "ED_ENGLISH": "DUBLIN SOMETHING",
            },
        }

        area = SmallArea.parse(geojson)
        small_areas = SmallAreas(geojson={"type": "FeatureCollection", "features": []})
        small_areas._data = [area]
        self.assertEqual(
            len(small_areas.get_around_point(0.501, 0.501, radius_km=1)), 1
        )

        self.assertEqual(
            len(small_areas.get_around_point(0.601, 0.601, radius_km=1)), 0
        )

        self.assertEqual(
            len(small_areas.get_around_point(0.601, 0.601, radius_km=100)), 1
        )

from irish_census.base import Base
from irish_census.utils import aggregate, parse_gender


def aggregate_occupation(data_list):
    return aggregate(
        [
            "male",
            "female",
        ],
        data_list,
    )


class Occupation(Base):
    dimension = "C03773V04522"

    def _parse(self, payload):
        return parse_gender(payload, self.dimension)

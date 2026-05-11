from irish_census.base import Base
from irish_census.utils import aggregate, parse_gender


def aggregate_social(data_list):
    return aggregate(
        [
            "male",
            "female",
        ],
        data_list,
    )


class Social(Base):
    dimension = "C03743V04492"

    def _parse(self, payload):
        return parse_gender(payload, self.dimension, reverse=False)

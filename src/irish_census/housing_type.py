from irish_census.base import Base
from irish_census.utils import aggregate, parse


def aggregate_housing_types(data_list):
    return aggregate(
        [
            "private_households",
        ],
        data_list,
    )


class HousingType(Base):
    dimension = "C03774V04528"

    def _parse(self, payload):
        return parse(payload, self.dimension)

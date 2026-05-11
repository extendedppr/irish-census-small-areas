from irish_census.base import Base
from irish_census.utils import aggregate, parse


def aggregate_households(data_list):
    return aggregate(
        [
            "persons_in_private_households",
            "private_households",
        ],
        data_list,
    )


class Households(Base):
    dimension = "C03774V04528"

    def _parse(self, payload):
        return parse(payload, self.dimension)

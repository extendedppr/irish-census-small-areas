from irish_census.base import Base
from irish_census.utils import aggregate, parse


def aggregate_type_of_occupancy(data_list):
    return aggregate(
        [
            "number_of_persons_in_permanent_private_households",
            "permanent_private_households",
        ],
        data_list,
    )


class TypeOfOccupancy(Base):
    dimension = "C03761V04510"

    def _parse(self, payload):
        return parse(payload, self.dimension)

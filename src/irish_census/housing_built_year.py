from irish_census.base import Base
from irish_census.utils import aggregate, parse


def aggregate_housing_built_year(data_list):
    return aggregate(
        [
            "permanent_private_households",
            "number_of_persons_in_permanent_private_households",
        ],
        data_list,
    )


class HousingBuiltYear(Base):
    dimension = "C03782V04531"

    def _parse(self, payload):
        return parse(payload, self.dimension)

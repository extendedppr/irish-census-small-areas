from irish_census.base import Base
from irish_census.utils import aggregate, parse_gender


def aggregate_marital_status(data_list):
    return aggregate(
        ["male", "female"],
        data_list,
    )


class MaritalStatus(Base):
    dimension = "C03739V04488"

    def _parse(self, values):
        return parse_gender(values, self.dimension, reverse=False)

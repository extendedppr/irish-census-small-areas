from irish_census.base import Base
from irish_census.utils import aggregate, parse


def aggregate_religion(data_list):
    return aggregate(["population"], data_list)["population"]


class Religion(Base):
    dimension = "C03775V04524"

    def _parse(self, payload):
        return parse(payload, self.dimension)

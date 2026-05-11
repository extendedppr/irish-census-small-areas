from irish_census.base import Base
from irish_census.utils import aggregate, parse


def aggregate_ethnicities(data_list):
    return aggregate(["usually_resident_population"], data_list)


class Ethnicity(Base):
    dimension = "C03740V04489"

    def _parse(self, payload):
        return parse(payload, self.dimension)

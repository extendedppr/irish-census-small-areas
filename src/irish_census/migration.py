from irish_census.base import Base
from irish_census.utils import aggregate, parse


def aggregate_migrations(data_list):
    return aggregate(
        [
            "usually_resident_population_by_birthplace",
            "usually_resident_population_by_citizenship",
        ],
        data_list,
    )


class Migration(Base):
    dimension = "C03785V04534"

    def _parse(self, payload):
        return parse(payload, self.dimension)

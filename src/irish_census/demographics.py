from irish_census.base import Base
from irish_census.utils import aggregate, parse_gender


def aggregate_demographics(data_list):
    return aggregate(
        [
            "male",
            "female",
        ],
        data_list,
    )


class Demographics(Base):
    dimension = "C03737V04485"

    def _parse(self, payload):
        return parse_gender(payload, self.dimension, reverse=False)

    def total_by_sex(self, sex):
        return int(sum(self.data[sex].values()))

    @property
    def total_population(self):
        return self.total_by_sex('both')

    @property
    def male_population(self):
        return self.total_by_sex('male')

    @property
    def female_population(self):
        return self.total_by_sex('female')

    @property
    def approx_mean_age(self):
        """
        Result will be close to average age / 100 but not quite since not granular
        """
        total_age = total_count = 0

        for age_band, count in self.data["both"].items():
            ages = age_band[4:]

            if "and_over" in ages:
                midpoint = int(ages.split("_")[0]) + 2.5
            else:
                low, high = map(int, ages.split("-"))
                midpoint = (low + high) / 2

            total_age += midpoint * count
            total_count += count

        return total_age / total_count if total_count else 0

    def __repr__(self):
        return f"<{self.model_name} total={self.total_population}>"

    def to_dict(self):
        return {"approx_mean_age": self.approx_mean_age, "data": self.data}

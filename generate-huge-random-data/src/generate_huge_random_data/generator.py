from io import StringIO, TextIOBase
from pathlib import Path
import random
import csv
import numpy as np
import pandas as pd

SAMPLE_SIZE_MAX = 2000
SAMPLE_SIZE_MIN = 1000
SAMPLE_SCORES_NUMBER = 50

sample_data_folder = Path("/sample_data")

NAMES_TXT = pd.read_csv(
    sample_data_folder.joinpath("USA-most-common-names.txt"),
    sep="\t",
    header=0,
)

LASTNAMES_TXT = pd.read_csv(
    sample_data_folder.joinpath("USA-most-common-lastnames.txt"),
    sep="\t",
    header=0,
)

CITIES_TXT = pd.read_csv(
    sample_data_folder.joinpath("USA-cities-by-population.txt"),
    sep="\t",
    header=0,
)


class Generator:
    def __init__(
        self,
        sample_size_max: int = SAMPLE_SIZE_MAX,
        sample_size_min: int = SAMPLE_SIZE_MIN,
        sample_scores_number=SAMPLE_SCORES_NUMBER,
    ):
        self.sample_size_max = sample_size_max
        self.sample_size_min = sample_size_min
        self.sample_scores_number = sample_scores_number
        self.samples = None

        self._names = NAMES_TXT.copy()
        self._names_total_weight = int(self._names["Count"].sum())
        self._names["weight"] = self._names["Count"] / self._names_total_weight

        self._lastnames = LASTNAMES_TXT.copy()
        self._lastnames_total_weight = int(self._lastnames["Count"].sum())
        self._lastnames["weight"] = (
            self._lastnames["Count"] / self._lastnames_total_weight
        )

        cities_extended = CITIES_TXT.copy()
        mask = cities_extended["City"].str.contains(
            "(Balance of|\\(balance\\))", case=False, regex=True
        )
        index_drop = cities_extended[mask].index
        cities_extended = cities_extended.drop(index_drop)

        mask = cities_extended["City"].str.contains(
            "(city|town|village|township)", case=False, regex=True
        )
        index_drop = cities_extended[~mask].index
        self._cities = cities_extended.drop(index_drop)

        self._cities_total_population = int(self._cities["Population"].sum())

        self._cities["weight"] = (
            self._cities["Population"] / self._cities_total_population
        )
        self._cities["City"] = (
            self._cities["City"]
            .str.replace(" city", "")
            .str.replace(" town", "")
            .str.replace(" village", "")
            .str.replace(" city (pt.)", "")
            .str.replace(" charter township", "")
        )

        self._cities["CityState"] = self._cities["City"] + "|" + self._cities["State"]

    def Generate(self):
        sample_size = random.randint(self.sample_size_min, self.sample_size_max)
        random_names = self._names.sample(
            n=sample_size, weights="weight", replace=True
        )["Name"]

        random_lastnames = self._lastnames.sample(
            n=sample_size, weights="weight", replace=True
        )["Lastame"]

        random_cities = (
            self._cities.sample(n=sample_size, weights="weight", replace=True)[
                "CityState"
            ]
            .str.split("|", n=1, expand=True)
            .rename(columns={0: "City", 1: "State"})
        )

        lines = []
        for _i, (_name, _lastname, _city, _state) in enumerate(
            zip(
                random_names,
                random_lastnames,
                random_cities["City"],
                random_cities["State"],
            )
        ):
            row = [_i, _name, _lastname, _city, _state]
            for _ in range(self.sample_scores_number):
                mu = random.randint(100, 1000)
                sigma = mu / 11.0
                row.append(random.gauss(mu=mu, sigma=sigma))
            lines.append(row)

        self.samples = lines

    @property
    def Samples(self, regenerate: bool = True):
        if regenerate or self.samples is None:
            self.Generate()
        return self.samples

    @property
    def SamplesCsvStr(self, regenerate: bool = True):
        if regenerate or self.samples is None:
            self.Generate()

        with StringIO(initial_value=None) as csvstr:
            scoreswriter = csv.writer(
                csvstr,
                quoting=csv.QUOTE_STRINGS,
            )
            scoreswriter.writerow(
                [
                    "ID",
                    "Firstname",
                    "Lastname",
                    "City",
                    "State",
                    *[f"Score_{i+1}" for i in range(self.sample_scores_number)],
                ]
            )
            scoreswriter.writerows(self.samples)

            return csvstr.getvalue()

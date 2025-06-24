"""Generate skewed samples of the rainbow colors"""

import random
import scipy.stats as sts

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
colors_len = len(colors)
locations = [
    "Wisconsin",
    "Maryland",
    "Missouri",
    "Indiana",
    "Tennessee",
    "Massachusetts",
    "Arizona",
    "Washington",
    "Virginia",
    "New_Jersey",
    "Michigan",
    "North_Carolina",
    "Georgia",
    "Ohio",
    "Illinois",
    "Pennsylvania",
    "New_York",
    "Florida",
    "Texas",
    "California",
]
sample_sizes = [
    3 * colors_len**2,
    5 * colors_len**2,
    11 * colors_len**2,
    13 * colors_len**2,
    17 * colors_len**2,
    19 * colors_len**2,
    23 * colors_len**2,
    29 * colors_len**2,
    31 * colors_len**2,
    37 * colors_len**2,
    41 * colors_len**2,
    43 * colors_len**2,
    47 * colors_len**2,
    53 * colors_len**2,
    59 * colors_len**2,
    61 * colors_len**2,
    67 * colors_len**2,
    71 * colors_len**2,
    73 * colors_len**2,
    79 * colors_len**2,
]
samples_count = len(sample_sizes)
samples = [[]] * samples_count
frequencies = [[0] * colors_len for _ in range(samples_count)]

for row in range(samples_count):
    sample = []
    for i in range(sample_sizes[row]):
        c = random.randint(0, 9) % 7
        frequencies[row][c] += 1
        sample += [c]

    samples[row] = sample

print(
    "|    Location    | Size_observed | Size_expected | Observed_Cell_Size | Expected_Cell_Size |",
    end="",
)
for c in colors:
    print(f" {c:>6} |", end="")

print(" statistic |  p-value  | IsUniform |")
print()

for row in range(samples_count):
    print(f"| {locations[row]:^14} ", end="")
    print(f"|      {sum(frequencies[row]):4}     ", end="")
    print(f"|      {sample_sizes[row]:4}     ", end="")
    print(f"|         {int(sum(frequencies[row])/colors_len):4d}       ", end="")
    print(f"|         {int(sample_sizes[row]/colors_len):4d}       |", end="")
    observed_values = []
    expected_values = []
    for c in range(colors_len):
        print(f" {frequencies[row][c]:6d} |", end="")
        expanded_color = [c] * frequencies[row][c]
        observed_values += expanded_color
        expected_color = [c] * int(sample_sizes[row] / colors_len)
        expected_values += expected_color

    statistic, pvalue = sts.kstest(observed_values, expected_values)
    isuniform = True
    if (
        pvalue < 0.05
    ):  # there's less than 5% chance the sample comes from a uniform distribution
        isuniform = False

    print(f" {statistic:9.7f} | {pvalue:9.7f} |   {isuniform!s:^5}   |", end="")
    print()

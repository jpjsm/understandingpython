"""Generate random signed numbers of 8, 16, 32, 64, 128 bits."""

import secrets
import time
import sys

import matplotlib.pyplot as plt
import scipy.stats as sts


def rnd(size: int = 4) -> int:
    if size not in [1, 2, 4, 8, 16]:
        size = 4
    mydecimalbytes = [0] * size
    _rnd = secrets.SystemRandom()
    mydecimalbytes = _rnd.randbytes(size)

    return int.from_bytes(mydecimalbytes, "little", signed=True)


if __name__ == "__main__":
    """Test numbers are uniformly generated."""

    print("Generating 8 bits numbers.", file=sys.stderr)
    buckets = 256
    items_per_bucket = 8192
    bucketcount_observed = [0] * buckets
    bucketcount_expected = [0] * buckets
    normalized_squareddifferences = [0] * buckets
    values_observed = []
    values_expected = []
    for i in range(buckets * items_per_bucket):
        r = rnd(1)
        bucketcount_observed[r + 128] += 1
        values_observed += [r + 128]

        bucketcount_expected[i % 256] += 1
        values_expected += [i % 256]

    assert sum(bucketcount_observed) == sum(bucketcount_expected), (
        f"[ERROR] Observed sample size ({sum(bucketcount_observed)} != "
        f"({sum(bucketcount_expected)}) expected sample size !!"
    )

    chiSquared = 0
    print("Label | Observed | Expected | (o-e)^2 / e |")
    print("------+---------+----------+--------------|")
    for i in range(buckets):
        normalized_squareddifferences[i] = (
            (bucketcount_observed[i] - bucketcount_expected[i]) ** 2
        ) / bucketcount_expected[i]
        chiSquared += normalized_squareddifferences[i]
        print(
            f"{i-128:5} |"
            f" {bucketcount_observed[i]:7}  "
            f"|{bucketcount_expected[i]:7}  "
            f"| {normalized_squareddifferences[i]:10.4f} |"
        )

    print("------+---------+----------+------------|")
    print()
    print(f"chiSquared: {chiSquared}")
    print()
    kstest_statistic, kstest_pvalue = sts.kstest(values_observed, values_expected)
    chisquare_statistic, chisquare_pvalue = sts.chisquare(
        bucketcount_observed, f_exp=bucketcount_expected
    )

    print(f" {kstest_statistic=:9.7f} | {kstest_pvalue=:9.7f} |")
    print(f" {chisquare_statistic=:9.7f} | {chisquare_pvalue=:9.7f} |")

    bins = [k for k in range(buckets)] + [256]
    min_observed = min(bucketcount_observed)
    #n, plot_bins, patches = plt.hist(values_observed, bins, bottom=-min_observed)
    n, plot_bins, patches = plt.hist(values_observed, bins)

    plt.show()

"""Understanding Kolmogorov-Smirnov test for uniform distributions."""

import random
import scipy.stats as sts

digits = [d for d in range(10)]
perfect = []
f_obs = []
f_exp = []
size = 1000
for d in digits:
    observations = size - 1 if d == 0 else (size + 1 if d == 9 else size)
    perfect += [d] * size
    f_obs += [size]
    f_exp += [size]

kstest_statistic, kstest_pvalue = sts.kstest(perfect, perfect)
chisquare_statistic, chisquare_pvalue = sts.chisquare(f_obs, f_exp=f_exp)


print(f" {kstest_statistic=:9.7f} | {kstest_pvalue=:9.7f} |")
print(f" {chisquare_statistic=:9.7f} | {chisquare_pvalue=:9.7f} |")

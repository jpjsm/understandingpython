"""Kolmogorov-Smirnov practical intro for Python programmers.

What is KS test good for
KS test is a powerful tool that exists in two versions. The 1-sample KS test can tell us whenter the sample is drawn from a certain distribution. This can tell us, for instance whether today’s incidents are anomalous compared to the annual average.

The 2-sample KS test can tell us whether 2 independent samples are drawn from the same continuous distribution. In the practical terms of our example, this can tell whether two groups of users behave differently.

Because the theoretical foundations of the KS test have been nicely covered elsewhere (https://www.real-statistics.com/non-parametric-tests/goodness-of-fit-tests/two-sample-kolmogorov-smirnov-test/ , thank you, Charles Zaiontz), here I will skip that and simply proceed to a very practical introduction for using it in Python.

The KS test (Kolmogorov-Smirnov) is a practical tool to provide objective
answers to such questions.
Here is a practical intro for Python programmers with little background in
statistics.
Source: https://ondata.blog/articles/kolmogorov-smirnov-test-a-practical-intro/
"""

import scipy.stats as sts
import random
import numpy as np

x = np.random.normal(loc=0.0, scale=1.0, size=1000)
print(f"x: len= {len(x)}, values={x}")
s = np.array(random.sample(x.tolist(), 100))
print(f"{s=}")
print(sts.kstest(rvs=s, cdf="norm"))

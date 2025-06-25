import time
import hashlib
import random
import string

import numpy as np

print(f"\n{'='*40}    Start test: 'MD5 performance'    {'='*40}")

BUCKETS = 31
ARRAY_SIZE = (200_000 // BUCKETS) * BUCKETS
DIFFERENT_STRINGS = 2_000
elapsed_by_strlen = {}
for k in range(DIFFERENT_STRINGS):

    bytesarr = bytearray(ARRAY_SIZE)
    for i in range(ARRAY_SIZE):
        bytesarr[i] = ord(
            string.printable[random.randint(0, len(string.printable) - 1)]
        )

    text = bytesarr.decode("utf-8")
    for i in range(1, ARRAY_SIZE + 1):
        s = text[0:i]
        s_len = len(s)
        start = time.perf_counter_ns()
        h = hashlib.md5(s.encode("utf-8")).hexdigest()
        elapsed_us = (time.perf_counter_ns() - start) / 1_000.0  # micro-seconds
        if s_len not in elapsed_by_strlen:
            elapsed_by_strlen[s_len] = []

        elapsed_by_strlen[s_len].append(elapsed_us)
        print(
            f"Processing string: {k+1: >12,} of {DIFFERENT_STRINGS: >12,}; "
            f"string length {s_len: >12,} of {ARRAY_SIZE: >12,}\r",
            sep="",
            end="",
        )


print(f"\n{'='*40}    Time to MD5 hash by string length    {'='*40}")
step = len(elapsed_by_strlen.keys()) // BUCKETS
str_lens = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, max(elapsed_by_strlen.keys())])
k = step
while k <= max(elapsed_by_strlen.keys()):
    str_lens.add(k)
    k += step

for _len in sorted(str_lens):
    data = np.array(elapsed_by_strlen[_len])
    du = data / _len
    p = np.percentile(data, [25, 50, 75, 90, 100])
    percentiles_str = f"{p[0]: >12,.3f} {p[1]: >12,.3f} {p[2]: >12,.3f} {p[3]: >12,.3f} {p[4]: >12,.3f}"
    print(
        f"string length: {_len: >8,}, samples: {len(elapsed_by_strlen[_len]): >8,}, p[25, 50, 75, 90, 100] => {percentiles_str} micro-seconds"
    )

print(f"\n{'='*40}    Finished test: 'MD5 performance'    {'='*40}")

from time import perf_counter_ns

from hpp.ch01.is_prime import IsPrime

numbers = [i for i in range(10_005_011, 10_005_092, 2)]
elapsed = 0
max_delta = 0
min_delta = perf_counter_ns()
number_max_delta = None
number_min_delta = None
results = []
for number in numbers:
    start = perf_counter_ns()
    isprime = IsPrime(number)
    delta = perf_counter_ns() - start
    r = (number, isprime, delta)
    elapsed += delta
    if delta < min_delta:
        min_delta = delta
        number_min_delta = r

    if delta > max_delta:
        max_delta = delta
        number_max_delta = r

    results.append(r)

print(f"Total elapsed time: {elapsed/1_000_000.0: > 12,f} ms")
print(f"Max   elapsed time: {max_delta/1_000_000.0: > 12,f} ms")
print(f"Min   elapsed time: {min_delta/1_000_000.0: > 12,f} ms")

for r in results:
    print(f"{r[0]: >12,} Is Prime: {r[1]!s: <6}, {r[2]/1_000_000.0: > 12,f} ms")

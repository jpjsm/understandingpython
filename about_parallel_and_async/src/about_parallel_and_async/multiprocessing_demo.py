## Reference
#  - https://docs.python.org/3/library/concurrency.html
#  - https://superfastpython.com/multiprocessing-in-python/
#  - https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.Pool
#  - https://docs.python.org/3/library/multiprocessing.html
#  - https://www.datacamp.com/tutorial/python-multiprocessing-tutorial


from multiprocessing import Pool
import time

from about_parallel_and_async.eratostenes import es_primo


if __name__ == "__main__":
    N = 20_000
    print(
        f"{'Array Length': >24} | {'Primes Found': >24} | {'MultiProcessing (secs)': >24} | {'Serial (secs)': >24} | {'Multiprocessing Performance Gain': >24}"
    )
    print(f"{'-'*25}+{'-'*26}+{'-'*26}+{'-'*26:}+{'-'*26:}")
    for i in range(10):
        n = N * (2**i)
        # first way, using multiprocessing
        start_time = time.perf_counter()
        with Pool() as pool:
            result = pool.map(es_primo, range(1, n))
        elapsed_multiprocessing = time.perf_counter() - start_time
        primes_multiprocessing = result.count(True)

        # second way, serial computation
        start_time = time.perf_counter()
        primes = []
        for x in range(1, n):
            if es_primo(x):
                primes.append(x)
        elapsed_serial = time.perf_counter() - start_time
        primes_serial = len(primes)
        if primes_multiprocessing != primes_serial:
            raise ValueError(
                f"ERROR: Number of primes differ for Array Length = {n:,}: results parallel = {primes_multiprocessing:,} != serial = {primes_serial}"
            )

        print(
            f"{n: >24,} | {primes_multiprocessing: >24,} | {elapsed_multiprocessing: >24,.6f} | {elapsed_serial: >24,.6f} | {elapsed_serial/elapsed_multiprocessing: >24,.6f}"
        )

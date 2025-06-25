## Reference
#  - https://docs.python.org/3/library/concurrency.html
#  - https://superfastpython.com/threading-in-python/
#    - https://superfastpython.com/threading-in-python/#Extend_the_Thread_Class
#  - https://builtin.com/data-science/multithreading-multiprocessing


from threading import Thread
import os
import time

from about_parallel_and_async.eratostenes import es_primo

num_cores = os.cpu_count()
max_threads = (num_cores * 8) // 10

print("Number of CPU cores:", num_cores, "Max number of threads:", max_threads)


class EsPrimoThread(Thread):
    def __init__(self, numbers_list: list[int], id: int | None = None):
        Thread.__init__(
            self, name=(f"EsPrimoThread_{id:0>6}" if isinstance(id, int) else None)
        )
        self.Primes = []
        self.numbers_list = numbers_list

    def run(self):
        for n in self.numbers_list:
            if es_primo(n):
                self.Primes.append(n)


if __name__ == "__main__":
    N = 20_000
    print(
        f"{'Array Length': >24} | {'Primes Found': >24} | {'Threading (secs)': >24} | {'Serial (secs)': >24} | {'Threading Performance Gain': >24}"
    )
    print(f"{'-'*25}+{'-'*26}+{'-'*26}+{'-'*26:}+{'-'*26:}")
    for i in range(10):
        n = N * (2**i)
        # first way, using threading
        start_time = time.perf_counter()
        primes = []
        thread_pool = {i: None for i in range(max_threads)}
        split_lists = {i: [] for i in range(max_threads)}
        for i in range(1, n):
            split_lists[i % max_threads].append(i)

        for t in range(max_threads):
            thread_pool[t] = EsPrimoThread(split_lists[t], id=t)
            thread_pool[t].start()

        while True:
            time.sleep(10.0 / 1000.0)  # 10 milli-seconds
            if all([not t.is_alive() for t in thread_pool.values()]):
                break

        for t in range(max_threads):
            primes += thread_pool[t].Primes

        elapsed_multiprocessing = time.perf_counter() - start_time
        primes_threading = len(primes)

        # second way, serial computation
        start_time = time.perf_counter()
        primes = []
        for x in range(1, n):
            if es_primo(x):
                primes.append(x)
        elapsed_serial = time.perf_counter() - start_time
        primes_serial = len(primes)
        if primes_threading != primes_serial:
            raise ValueError(
                f"ERROR: Number of primes differ for Array Length = {n:,}: results parallel = {primes_threading:,} != serial = {primes_serial}"
            )

        print(
            f"{n: >24,} | {primes_threading: >24,} | {elapsed_multiprocessing: >24,.6f} | {elapsed_serial: >24,.6f} | {elapsed_serial/elapsed_multiprocessing: >24,.6f}"
        )

import random
from time import perf_counter_ns

from hpp.ch01.search_needle_haystack import (
    search_fast,
    search_slow,
    search_unknown_list,
    search_unknown_tuple,
)

search = {
    "search_fast": search_fast,
    "search_slow": search_slow,
    "search_unknown_list": search_unknown_list,
    "search_unknown_tuple": search_unknown_tuple,
}

search_functions = search.keys()

results = {
    key: {
        "total_elapsed_ns": 0,
        "max_elapsed_ns": -1,
        "min_elapsed_ns": perf_counter_ns(),
        "iterations": 0,
    }
    for key in search_functions
}

HAYSTACK_SIZES = [1_000, 10_000, 100_000, 1_000_000, 10_000_000]
ITERATIONS = 10_000

for HAYSTACK_SIZE in HAYSTACK_SIZES:
    print(f"{'*'*20}    HAYSTACK_SIZE = {HAYSTACK_SIZE: >12,}    {'*'*20}")
    haystack = []
    for i in range(HAYSTACK_SIZE):
        haystack.append(random.randint(10_000_000, 99_999_999))

    for i in range(ITERATIONS):
        needle = haystack[random.randint(0, HAYSTACK_SIZE - 1)]
        for search_function in search_functions:
            start = perf_counter_ns()
            _ = search[search_function](haystack=haystack, needle=needle)
            delta = perf_counter_ns() - start
            results[search_function]["total_elapsed_ns"] += delta
            results[search_function]["iterations"] += 1

            if delta < results[search_function]["min_elapsed_ns"]:
                results[search_function]["min_elapsed_ns"] = delta

            if delta > results[search_function]["max_elapsed_ns"]:
                results[search_function]["max_elapsed_ns"] = delta

    for key, result in sorted(results.items(), key=lambda i: i[1]["total_elapsed_ns"]):
        elapsed_secs = result["total_elapsed_ns"] / 1_000_000_000.0
        min_secs = result["min_elapsed_ns"] / 1_000.0
        avg_secs = (result["total_elapsed_ns"] / 1_000.0) / results[search_function][
            "iterations"
        ]
        max_secs = result["max_elapsed_ns"] / 1_000.0

        print(
            f"{key: <32}: total time: {elapsed_secs: >12,.3f} secs; total iterations: {ITERATIONS: > 7,}; "
            f"(min; avg; max) µSecs: ({min_secs: >12,.3f}; {avg_secs: >12,.3f}; {max_secs: >12,.3f}) µSecs"
        )

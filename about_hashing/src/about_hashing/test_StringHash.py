from datetime import datetime
import time
import random
import string

from about_hashing.stringhash import StringHash, M

print(f"\n{'='*40}    Start test: 'StringHash'    {'='*40}")

TOTAL_BUCKETS = 31
ARRAY_SIZE = (5_000 // TOTAL_BUCKETS) * TOTAL_BUCKETS
DIFFERENT_STRINGS = 5000

hashes = {}
repeated_hashes = set()
generated_strings = set()
collisions = 0
tested = 0
for lap in range(DIFFERENT_STRINGS):
    bytesarr = bytearray(ARRAY_SIZE)
    for i in range(ARRAY_SIZE):
        bytesarr[i] = ord(
            string.printable[random.randint(0, len(string.printable) - 1)]
        )

    text = bytesarr.decode("utf-8")
    # print(f"{k: >12,}: {repr(text)}")
    for i in range(1, ARRAY_SIZE + 1):
        s = text[0:i]

        if s in generated_strings:
            # no need to track repeated strings
            continue

        generated_strings.add(s)

        tested += 1

        start = time.perf_counter_ns()
        h = StringHash(s)
        elapsed_ms = (
            time.perf_counter_ns() - start
        ) / 1_000_000  # nano-seconds to milli-seconds

        if h in hashes:
            hashes[h]["count"] += 1
            hashes[h]["strings"].append(s)
            collisions += 1
            repeated_hashes.add(h)
        else:
            hashes[h] = {"count": 1, "strings": [s]}

        # print(
        #    f"collision ratio: {collisions: >12,}/{tested: >12,} ({collisions/tested: >12,.8f}), "
        #    f"elapsed {elapsed_ms: >12,.3f} ms, elapsed {elapsed_ms/len(s): >12,.3f} ms/char; \r",
        #    sep="",
        #    end="",
        # )

    print()
    hash_count = len(hashes)
    frequency = float(hash_count) / TOTAL_BUCKETS
    bucket_size = M // TOTAL_BUCKETS
    buckets_overflow = M % TOTAL_BUCKETS
    buckets = [0] * (TOTAL_BUCKETS + 1)
    for k in hashes.keys():
        bucket_id = k // bucket_size
        buckets[bucket_id] += hashes[k]["count"]

    print(f"\n{'='*40}    Hash Frequencies    {'='*40}")
    for k in range(len(buckets)):
        print(f"{k*bucket_size: >32,} : {buckets[k]}")
    print(f"\n{'='*40}    Descriptors    {'='*40}")
    print(
        f"collision ratio             : {collisions: >8,}/{tested: >12,} ({collisions/tested: >12,.8f})"
    )
    print(f"Hash count                : {hash_count: >32,}")
    print(f"Expected frequency        : {frequency: >36,.3f}")
    print(f"Total buckets             : {TOTAL_BUCKETS: >32,}")
    print(f"Bucket size               : {bucket_size: >32,}")
    print(f"Bucket overflow           : {buckets_overflow: >32,}")
    print(f"repeated hashes           : ")
    for h in sorted(repeated_hashes):
        print(f"\t{h: <32,}: {hashes[h]['strings']}")

    print(f"\n{'.'*40}    | lap: {lap:>9,} |    {'.'*40}\n")


print(f"\n{'='*40}    Finished test: 'StringHash'    {'='*40}")

print(f"\n{'='*40}    DONE    {'='*40}")

"""Unrelated tools used through the project."""
import time


def ns2ms(nanoseconds: int | float) -> float:
    """Converts nanoseconds to milliseconds.

    :param nanoseconds: the nanoseconds to convert.

    :returns: milliseconds.
    """
    return float(nanoseconds / 1e6)


def rnd(size: int = 4) -> int:
    if size not in [1, 2, 4, 8, 16]:
        size = 4
    mydecimalbytes = [0] * size
    for i in range(size):
        condition = True
        while condition:
            n = time.perf_counter_ns() // 100
            n = n % 10000
            condition = n > 9983  # removing tail preferences

        mydecimalbytes[i] = n % 256

    return int.from_bytes(mydecimalbytes, "big", signed=True)

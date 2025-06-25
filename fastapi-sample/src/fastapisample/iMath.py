"""Simple integer arithmetic algorithms"""

from typing import Tuple


def iDiv(N: int, D: int) -> Tuple[int, int]:
    n = int(N)
    d = int(D)
    s = (-1 if n < 0 else 1) * (-1 if d < 0 else 1)
    n = -n if n < 0 else n
    d = -d if d < 0 else d

    if d == 0:
        raise ValueError("Argument Exception: division by zero")

    q = 0

    while n >= d:
        r = d
        qq = 1
        while n >= r:
            r <<= 1
            qq <<= 1

        r >>= 1
        qq >>= 1

        n -= r
        q += qq

    return (s * q, n)


def iProd(A: int, B: int) -> int:
    a = int(A)
    b = int(B)
    s = -1 if (a < 0) ^ (b < 0) else 1
    a = -a if a < 0 else a
    b = -b if b < 0 else b

    if a == 0 or b == 0:
        return 0

    p = 0
    while b > 0:
        if b & 0b1:
            p += a

        a <<= 1
        b >>= 1

    return s * p

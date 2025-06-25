## Reference:
#  - https://www.geeksforgeeks.org/string-hashing-using-polynomial-rolling-hash-function/
#  - https://cp-algorithms.com/string/string-hashing.html
#  - https://en.wikipedia.org/wiki/Rolling_hash
from pathlib import Path

from about_hashing.FastModPower import ModPower
from about_hashing.circularrotation import CRR

M1, M2 = 2_147_483_629, 2_147_483_631
M = 2**64

P1, P2 = 29, 71

B1, B2 = 11, 13


def StringHash(text: str) -> int | None:
    if text is None:
        return None

    text_bytes = str(text).encode(encoding="utf-8")
    len_text_bytes = len(text_bytes)
    r1, r2 = B1, B2
    for i in range(len_text_bytes):
        r1 += text_bytes[i] * ModPower(i, P1, M1)
        r2 += text_bytes[i] * ModPower(i, P2, M2)
        if r1 >= M1:
            r1 %= M1
        if r2 >= M2:
            r2 %= M2
    h = (r2 << 31) + r1
    nh = CRR(h, len_text_bytes)
    return nh

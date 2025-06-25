import asyncio
from typing import Tuple
import psutil
from primes import Primes
from iMath import iProd, iDiv
from time import sleep


async def async_iDiv(N: int, D: int) -> Tuple[int, int]:
    return iDiv(N, D)


if __name__ == "__main__":
    # before = dict([cpu for cpu in psutil.cpu_times()])
    before = dict(
        [
            (_name, getattr(psutil.cpu_times(), _name))
            for _name in psutil.cpu_times()._fields
        ]
    )
    p = 1
    for n in Primes[600:700]:
        p = iProd(p, n)

    results = [iDiv(p, d) for d in Primes[700:800]]

    # print(f"{p:120,d} // {d:8,d} = {q:,d} R:{r:,}")
    print(results)

    middle = dict(
        [
            (_name, getattr(psutil.cpu_times(), _name))
            for _name in psutil.cpu_times()._fields
        ]
    )
    sleep(10)
    last = dict(
        [
            (_name, getattr(psutil.cpu_times(), _name))
            for _name in psutil.cpu_times()._fields
        ]
    )

    for key in before:
        print(f"CPU intensive: {key} = {middle[key] - before[key]}")
        print(f"CPU relaxed  : {key} = {last[key] - middle[key]}")
        print()

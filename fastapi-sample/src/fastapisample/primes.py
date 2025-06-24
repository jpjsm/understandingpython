"""Initial prime numbers list."""

import json
from shutil import copyfile
from iMath import iDiv, iProd
from typing import Tuple
import pathlib


class primes:
    """All prime numbers known to this class ;)"""

    folder = pathlib.Path(__file__).parent
    initialprimes_filename = str(pathlib.Path.joinpath(folder, "initialprimes.json"))
    initialprimes_bak_filename = str(
        pathlib.Path.joinpath(folder, "initialprimes.json.bak")
    )

    knownprimes = []
    with open(initialprimes_filename, "r") as _initial_primes:
        knownprimes = json.load(_initial_primes)

    knownprimes = sorted(knownprimes)

    primes_set = set(knownprimes)

    @staticmethod
    def nextprimes(rangesize: int) -> list[int]:
        """Get the next primes in the range between the last one in the list
        and the last one + rangesize.

        Note: rangesize will be adjusted if it is less than 64K or over 128M"""
        _64K = 0xFFFF
        _128M = 0x7FFFFFF
        rangesize = rangesize if rangesize >= _64K else _64K
        rangesize = rangesize if rangesize <= _128M else _128M

        # For small sets of initial primes, lastprime + rangesize < lastprime^2
        # otherwise sieving would be much harder

        lastprime = primes.knownprimes[-1]
        candidateupperlimit = iProd(lastprime, lastprime) - 1
        if (rangesize + lastprime) > candidateupperlimit:
            # We divide by 2, because the sieve only takes odd numbers
            # (no need to have even nubers and cross them out on the
            # first pass)
            rangesize = iDiv(candidateupperlimit - lastprime, 2)[0] + 1

        firstcandidate = lastprime + 2

        # The sieve array  maps odd numbers from last-known-prime + 2
        # (aka the next prime candidate) up to
        # (last-known-prime + 2) + 2 * rangesize
        sieve = [0] * rangesize
        for p in primes.knownprimes[1:]:
            q, r = iDiv(firstcandidate, p)

            i = 0
            if r == 0:
                i = 0
            else:
                if (r & 0b1) == 0:
                    # r is even => p*q is odd => sieve is aligned with p*q
                    # getting the starting point on the sieve
                    i = p - iDiv(r, 2)[0]
                else:
                    i = iDiv(p * (q + 1) - firstcandidate, 2)[0]

            while i < rangesize:
                sieve[i] = 1
                i += p

        for i in range(0, rangesize):
            if sieve[i] == 0:
                newprime = firstcandidate + 2 * i
                primes.knownprimes.append(newprime)

        primes.primes_set = set(primes.knownprimes)

        # Let's make a copy of existing 'initialprimes.json' file,
        # before overwriting it
        copyfile(
            primes.initialprimes_filename,
            primes.initialprimes_bak_filename,
        )
        with open(primes.initialprimes_filename, "w") as _initial_primes:
            json.dump(
                primes.knownprimes,
                _initial_primes,
            )

    @staticmethod
    def isprime(n: int) -> bool:
        n = int(n)
        negative = n < 0
        if negative:
            n = -n

        if n == 0:
            return False

        if n == 1:
            return False

        lastprime = primes.knownprimes[-1]
        while n > iProd(lastprime, lastprime):
            primes.nextprimes(iDiv(n - lastprime + 1, 2)[0])
            lastprime = primes.knownprimes[-1]

        if n in primes.primes_set:
            return True

        for p in primes.knownprimes:
            if iDiv(n, p)[1] == 0:
                return False

            if n < iProd(p, p):
                break

        return True

    @staticmethod
    def factors(n: int) -> list[int]:
        _factors = []
        lastprime = primes.knownprimes[-1]
        while (iDiv(n, 2)[0] + 1) > lastprime:
            primes.nextprimes(iDiv(n - lastprime + 1, 2)[0])
            lastprime = primes.knownprimes[-1]

        for p in primes.knownprimes:
            if p > n:
                break

            q, r = iDiv(n, p)
            while r == 0:
                _factors.append(p)
                n = q
                q, r = iDiv(n, p)

        return _factors

    @staticmethod
    def tryaddprime(n: int) -> Tuple[bool, int, str, list[int]]:
        n = int(n)
        negative = n < 0
        if negative:
            n = -n

        if n == 0:
            return (False, n, "Zero (0) is not a prime number", [])

        if n == 1:
            return (False, n, "One (1) is not a prime number", [])

        if not primes.isprime(n):
            return (False, n, "Not a prime number", primes.factors(n))

        if n not in primes.primes_set:
            primes.nextprimes((n - primes.knownprimes[-1]))
            primes.primes_set.add(n)

        return (True, n, "Added", [1, n])


if __name__ == "__main__":
    n = 11 * 13 * 29 * 31 + 2
    isprime = primes.isprime(n)
    assert isprime is False
    print(f"Is {n} prime: {isprime}")
    if not isprime:
        factors = primes.factors(n)
        print(f"{n} factors: {factors}")
        assert factors == [3, 42853]

    n = 3456789
    isprime = primes.isprime(n)
    assert isprime is False
    print(f"Is {n} prime: {isprime}")
    if not isprime:
        factors = primes.factors(n)
        print(f"{n} factors: {factors}")
        assert factors == [3, 7, 97, 1697]

    n = (0b1 << 19) - 1  # Mersenne prime
    isprime = primes.isprime(n)
    assert isprime is True
    print(f"Is {n} prime: {isprime}")
    if not isprime:
        print(f"{n} factors: {primes.factors(n)}")

    twins = 0
    for i in range(1, len(primes.knownprimes)):
        if (primes.knownprimes[i] - primes.knownprimes[i - 1]) == 2:
            twins += 1

    print("primes info:")
    print(f"-   Largest prime recorded: {primes.knownprimes[-1]:30,d}")
    print(f"-   Primes recorded       : {len(primes.knownprimes):30,d}")
    print(f"-   Twin primes recorded  : {twins:30,d}")

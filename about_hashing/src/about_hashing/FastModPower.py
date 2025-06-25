## Reference:
#  - https://en.wikipedia.org/wiki/Modular_exponentiation
#  - https://www-users.cse.umn.edu/~garrett/crypto/Code/FastPow_Python.html
#  - https://www.quora.com/How-can-we-calculate-a-b-c-mod-n
import json
import pickle
from pathlib import Path

from about_hashing.ModPower_Cache import Cache

modpower_cache_path = "modpower_cache.pkl"

modpower_cache = Cache
if len(modpower_cache) == 0 and Path(modpower_cache_path).exists():
    with open(modpower_cache_path, "rb") as infile:
        try:
            modpower_cache = pickle.load(infile, encoding="utf-8")
        except:
            pass  # Ignore error and regenerate


def save_ModPowerCache():
    with open(modpower_cache_path, "wb") as outfile:
        pickle.dump(modpower_cache, outfile)


def generate_ModPowerCachePy():
    modpower_cache_str = json.dumps(modpower_cache)
    src = f"""
import json        
ModPower_Cache = json.loads('{modpower_cache_str}')
"""
    with open(
        Path(__file__).parent.joinpath("ModPower_Cache.py"), "w", encoding="utf-8"
    ) as outfile:
        outfile.write(src)


def ModPower(exponent: int, base: int, modulus: int) -> int:
    if base <= 0 or modulus <= 0:
        raise ValueError(
            "'base' and 'modulus' arguments must be integers greater than zero"
        )

    if exponent < 0:
        raise ValueError(
            "'exponent' argument must be an integer greater than or equal zero"
        )

    if modulus == 1:
        return 0

    if exponent == 0:
        return 1

    if base == 1:
        return 1

    key = f"{modulus} {base} {exponent}"
    if key in modpower_cache:
        return modpower_cache[key]

    r = 1
    while exponent > 0:
        if exponent & 1:
            r = (base * r) % modulus
            if r >= modulus:
                r %= modulus
            exponent -= 1
        else:
            base *= base
            if base > modulus:
                base %= modulus

            exponent >>= 1

    modpower_cache[key] = r

    return r


if __name__ == "__main__":
    generate_ModPowerCachePy()

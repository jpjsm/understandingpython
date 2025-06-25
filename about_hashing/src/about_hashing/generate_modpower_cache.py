from about_hashing.FastModPower import ModPower, save_ModPowerCache
from about_hashing.stringhash import M1, M2, P1, P2

print(f"\n{'='*40}    Start test: 'modpower'    {'='*40}")

for M in [
    M1,
    M2,
]:
    for base in [
        P1,
        P2,
    ]:
        for i in range(200_000):
            print(
                f"exponent: {i: >6,}; base: {base: >3,}; modulus: {M: >12,}\r",
                sep="",
                end="",
            )
            assert ModPower(i, base, M) == (base**i) % M

save_ModPowerCache()

from about_hashing.FastModPower import ModPower

print(f"\n{'='*40}    Start test: 'modpower'    {'='*40}")

for M in [
    2_147_483_629,
    2_147_483_631,
]:
    for base in [
        41,
        43,
    ]:
        for i in range(20_000):
            print(
                f"exponent: {i: >6,}; base: {base: >3,}; modulus: {M: >12,}\r",
                sep="",
                end="",
            )

            assert ModPower(i, base, M) == (base**i) % M

print(f"\n{'='*40}    Finished test: 'modpower'    {'='*40}")
print(f"\n{'='*40}    DONE    {'='*40}")

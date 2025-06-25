import math


def julia(z: complex, c) -> complex:
    return z * z + c


z = -1.8 - 1.8j

print(abs(z))

c = -0.62772 - 0.42193j
z = 0 + 0j

for i in range(9):
    z = julia(z, c)
    print(f"{i}: z={z: .5f}, abs(z)={abs(z):0.3f}, c={c: .5f}")

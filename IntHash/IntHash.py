class IntClass:
    def __init__(self, i: int) -> None:
        self.i = i

    def flip16(self) -> int:
        flip = self.i
        flip1 = ((flip & 0b_1010_1010_1010_1010_1010_1010_1010_1010) >> 1) + (
            (flip & 0b_0101_0101_0101_0101_0101_0101_0101_0101) << 1
        )

        flip2 = ((flip1 & 0b_1100_1100_1100_1100_1100_1100_1100_1100) >> 2) + (
            (flip1 & 0b_0011_0011_0011_0011_0011_0011_0011_0011) << 2
        )

        flip4 = ((flip2 & 0b_1111_0000_1111_0000_1111_0000_1111_0000) >> 4) + (
            (flip2 & 0b_0000_1111_0000_1111_0000_1111_0000_1111) << 4
        )

        flip8 = ((flip4 & 0b_1111_1111_0000_0000_1111_1111_0000_0000) >> 8) + (
            (flip4 & 0b_0000_0000_1111_1111_0000_0000_1111_1111) << 8
        )

        flip = ((flip8 & 0b_1111_1111_1111_1111_0000_0000_0000_0000) >> 16) + (
            (flip8 & 0b_0000_0000_0000_0000_1111_1111_1111_1111) << 16
        )

        return flip


if __name__ == "__main__":
    """
    Generating uniformely distributed hash values by swapping bits

    Note:
    After a series of analysis, swapping 1, 2, 4, 8, 16 bits (in this order)
    is equivalent to reverse the bits in a 32 bits word
    """

    # TL ; DR
    symbols = ["-", "\\", "|", "/"]

    hashes = {}
    flips = {}

    print()
    for n in range(-2147483648, 2147483648):
        foo = IntClass(n)
        h = foo.i.__hash__()
        f = foo.flip16()

        if h not in hashes:
            hashes[h] = []

        hashes[h].append(n)

        if f not in flips:
            flips[f] = []

        flips[f].append(n)

        if len(hashes[h]) > 1:
            print(
                f"                          Collisions detected in Hashes[{h}]: [{hashes[h]}]\r",
                end="",
            )

        if len(flips[f]) > 1:
            print(
                f"                          Collisions detected in Flips[{f}]: [{flips[f]}]\r",
                end="",
            )

        if (n & 0b_1111_1111_1111_1111_1111) == 0:
            print("     {0:20n}\r".format(n), end="")

        print("   \r{0}\r".format(symbols[n % len(symbols)]), end="")

    print("finished.")

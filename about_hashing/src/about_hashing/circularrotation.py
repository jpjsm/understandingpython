import struct


def CRR(n: int, r: int, bits=64) -> int:
    format_code = {8: ">B", 16: ">H", 32: ">I", 64: ">Q"}
    if not isinstance(n, int):
        raise ValueError("'n' MUST be of integer type.")

    if n >= 18446744073709551616:
        raise ValueError("'n' MUST be less than 2**64.")

    if n < -9_223_372_036_854_775_808:
        raise ValueError("'n' MUST be greater than -2**63.")

    if bits < 0:
        raise ValueError("'bits' MUST be greater than zero.")

    if bits not in [8, 16, 32, 64]:
        if bits < 8:
            bits = 8
        elif bits < 16:
            bits = 16
        elif bits < 32:
            bits = 32
        else:
            bits = 64

    if r < 0:
        raise ValueError("'r' MUST be greater than zero.")

    r %= bits  # it's a circular rotation

    n_bytes = struct.pack(format_code[bits], n)
    n = (struct.unpack(format_code[bits], n_bytes))[0]
    mask = (1 << bits) - 1
    return (n >> r) | ((n << (bits - r)) & mask)

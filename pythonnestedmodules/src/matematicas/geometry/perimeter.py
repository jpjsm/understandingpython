"""calculates the perimer of any flat and closed geometric figure."""


from matematicas import number
from matematicas.arith.float.operations import add


def perimeter(sides: list[float]) -> float:
    """given a list of sides return the perimeter."""

    p = 0.0
    for s in [f for f in sides if isinstance(f, number())]:
        p = add(p, s)
    return p

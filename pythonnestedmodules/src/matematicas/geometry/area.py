"""Let's get some areas."""

from matematicas.arith.float.operations import multiply


def trianglearea(b: float, h: float) -> float:
    return multiply(multiply(0.5, b), h)


def squarearea(side: float) -> float:
    return multiply(side, side)


def rectangulearea(length: float, width: float) -> float:
    return multiply(length, width)

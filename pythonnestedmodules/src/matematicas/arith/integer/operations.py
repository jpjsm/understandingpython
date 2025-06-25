"""Implements basic arithmetic operations using integer types."""


from typing import Tuple


def add(a: int, b: int) -> int:
    return int(a) + int(b)


def substract(a: int, b: int) -> int:
    return int(a) - int(b)


def multiply(a: int, b: int) -> int:
    return int(a) * int(b)


def divide(a: int, b: int) -> Tuple[int, int]:
    return int(a) // int(b), int(a) % int(b)

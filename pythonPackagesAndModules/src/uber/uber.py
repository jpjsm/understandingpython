"""Understanding packages and modules."""
from sys import stderr


def greetings():
    print(f"Hello, {__file__}!", file=stderr)

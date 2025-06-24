"""Understanding packages and modules."""
from sys import stderr


def saludos():
    print(f"Hola, {__file__}!", file=stderr)

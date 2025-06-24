"""Unit tests for geometric operations."""

from matematicas.geometry.perimeter import perimeter
from matematicas.geometry.area import trianglearea, squarearea, rectangulearea

if __name__ == "__main__":
    assert abs(perimeter([1, 2.0, 3.14, "4", None, "one"]) - 6.14) <= 1e-15, (
        'abs(perimeter([1, 2.0, 3.14, "4", None, "one"]) - 6.14) <= 1e-15'
        f' != {abs(perimeter([1, 2.0, 3.14, "uno", None, "one"]) - 6.14)}'
    )
    assert abs(trianglearea(8, 4) - 16.0) <= 1e-15, (
        "abs(trianglearea(8, 4) - 16.0) <= 1e-15 != "
        f"{abs(trianglearea(8, 4) - 16.0)}"
    )
    assert (
        abs(squarearea(5.0) - 25.0) <= 1e-15
    ), f"abs(squarearea(5.0) - 25.0) <= 1e-15 != {abs(squarearea(5.0) - 25.0)}"
    assert abs(rectangulearea(3, 7.0) - 21.0) <= 1e-15, (
        "abs(rectangulearea(3, 7.0) - 21.0) <= 1e-15 != "
        f"{abs(rectangulearea(3, 7.0) - 21.0)}"
    )

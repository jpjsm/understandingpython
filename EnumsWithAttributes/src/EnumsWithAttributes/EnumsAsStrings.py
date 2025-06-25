# Attributions
# ----------------------------------------------------------
# Title: Add additional attributes to enum members in Python
# URL: https://rednafi.github.io/reflections/add-additional-attributes-to-enum-members-in-python.html
# Author: Redowan Delowar, Email: redowan.nafi@gmail.com
# ----------------------------------------------------------

from __future__ import annotations

from enum import Enum


class Color(str, Enum):
    RED = "Red"
    GREEN = "Green"
    BLUE = "Blue"


# Print individual members.
print(f"{Color.RED=}")

# Print name as a string.
print(f"{Color.GREEN.name=}")

# Print value.
print(f"{Color.BLUE.value=}")

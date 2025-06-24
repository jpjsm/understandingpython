"""Add additional attributes to enum members in Python.

Explanation
----------------------------------------------------------
Override the __new__ method of the class Color.

Method __new__ is a special class method that you don't need to decorate
with the @classmethod decorator. It gets executed during the creation of
the Color object; before the __init__ method.
Other than the first argument cls, you can define the __new__ method with
any number of arbitrarily named arguments.
In this case, the value of each member of Color will have three
elements: title, hex_code, and description.
So, the __new__ method is defined to accept those arguments.

In the following line, the str class was initialized via
obj = str.__new__(cls, title) and then title was assigned to the newly
created string object via obj._value_=title.

This line is crucial; without it, the enum won't operate at all.
This assignment makes sure that the Enum.member.value will return a string value.

In the next two lines, hex_code and description were attached to the member values
via the obj.hex_code=hexcode and obj.description=description statements respectively.
----------------------------------------------------------

Attributions
----------------------------------------------------------
Title: Add additional attributes to enum members in Python
URL: https://rednafi.github.io/reflections/add-additional-attributes-to-enum-members-in-python.html
Author: Redowan Delowar, Email: redowan.nafi@gmail.com
----------------------------------------------------------
"""


from __future__ import annotations

from enum import Enum


class Color(str, Enum):
    # Declaring the additional attributes here keeps mypy happy.
    hex_code: str
    description: str

    def __new__(cls, title: str, hex_code: str = "", description: str = "") -> Color:

        obj = str.__new__(cls, title)
        obj._value_ = title

        obj.hex_code = hex_code
        obj.description = description
        return obj

    RED = ("Red", "#ff0000", "Ruby Red")
    GREEN = ("Green", "#00ff00", "Guava Green")
    BLUE = ("Blue", "#0000ff", "Baby Blue")


# Access the elements of the values of the members by names.
print(f"{Color.RED.name=}")
print(f"{Color.RED.value=}")
print(f"{Color.BLUE.hex_code=}")
print(f"{Color.GREEN.description=}")

# Iterate through all the memebers.
for c in Color:
    print(
        f"title={c.value}, "
        + f"hex_code={c.hex_code}, "
        + f"description={c.description}"
    )

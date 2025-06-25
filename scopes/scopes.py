top = "At the top"

print(f"{top=}")


def func1():
    global top
    top = "At the top, with a new look"


func1()

print(f"{top=}")

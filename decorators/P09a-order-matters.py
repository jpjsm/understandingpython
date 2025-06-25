from decorators09 import timer, debug
from time import sleep


@timer
@debug
def function1(*args, **kwargs):
    print("starting function1")
    sleep(0.5)
    return "finished function1"


@debug
@timer
def function2(*args, **kwargs):
    print("starting function2")
    sleep(0.5)
    return "finished function2"


if __name__ == "__main__":
    function1("Hello", 0, True, None, k1="Key1")
    function2("Hello", 0, True, None, k1="Key1")

class foo:

  def __init__(foo, a = "", b = 0, c = False):
    foo.alpha = str(a)
    foo.bravo = int(b)
    foo.charlie = bool(c)


if __name__ == "__main__":
    import json
    f = foo()
    print(json.dumps(f.__dict__))

    f = foo("Hello world", 33, True)
    print(json.dumps(f.__dict__))

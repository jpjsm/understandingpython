import __future__
import multiprocessing

def foo(a):
    if a % 33 == 0:
        raise Exception('Multiple of 33 !!')

    return a * a

def foo_wrapper(a):
    foo_result = None
    try:
        foo_result = foo(a)
    except Exception:
        pass
    return foo_result

if __name__ == "__main__":
    # raise Exception(dir(multiprocessing.multiprocessing))
    processpool = multiprocessing.Pool(5)
    results = None
    try:
        results = processpool.map(foo_wrapper, range(1,101))
    except Exception as identifier:
        pass
    print(results)

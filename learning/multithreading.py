import multiprocessing.dummy as multithreadpool
import random
import time

def squareof(x):
    print "Calculating {0} * {0} !!".format(x)
    time.sleep(random.randint(1,5))
    print "Done !! {0} * {0} = {1}".format(x, x * x)
    return (x, x * x)

def parallel_execution(calculations = 100):
    numbers_to_square = range(1, calculations + 1)
    max_threads = multithreadpool.cpu_count()
    thread_pool = multithreadpool.JoinableQueue(max_threads)
    while len(numbers_to_square) > 0:
        while not thread_pool.full():
            

 
# create a decorator function to calculate run time of
# a fast function and a slow function

import time

current_time = time.time()
# print(current_time)


def speed_calc_decorator(function):
    def wrapper_function():
        start = time.time()
        function()
        end = time.time()
        run_time = end - start
        print(run_time)

    return wrapper_function


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i


fast_function()
slow_function()
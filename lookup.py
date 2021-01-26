import timeit
import random

RandomListOfIntegers = [random.randint(1, 10) for iter in range(1000000)]

def lookup_function_1():
    value = 10
    for i in RandomListOfIntegers:
        if i == value:
            return True
    return False


print(timeit.timeit(lookup_function_1))


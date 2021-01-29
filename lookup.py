import timeit
import random

RandomListOfIntegers = [random.randint(1, 10) for iter in range(1000000)]

def look_up(value):
    return RandomListOfIntegers[value]

for i in range (0, 10000001, 1000):
    print (i, timeit.timeit('%s'%look_up(i)))


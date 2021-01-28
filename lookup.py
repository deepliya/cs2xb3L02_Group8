import timeit
import random

RandomListOfIntegers = [random.randint(1, 10) for iter in range(1000001)]

def look_up(value):
    return RandomListOfIntegers[value]

for i in range (0, 1000001, 1):
    print (i, timeit.timeit('%s'%look_up(i))) 


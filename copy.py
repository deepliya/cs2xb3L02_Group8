import timeit
import random


def copy_function(lst):
    return lst.copy()


for i in range(0, 1001, 50):

    lst = [random.randint(1, 10) for iter in range(i)]
    print(len(lst), timeit.timeit('%s'%copy_function(lst)))



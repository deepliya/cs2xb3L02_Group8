import timeit
import random


def copy_function(lst):
    copied_lst = lst.copy()
    return copied_lst


for i in range(1, 1001, 50):

    lst = [random.randint(1, 10) for iter in range(i)]
    print(timeit.timeit('%s'%copy_function(lst)))



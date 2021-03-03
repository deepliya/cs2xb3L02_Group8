import timeit
import random 
from heap.py import *

def create_random_list(n):
    return [random.random() for _ in range(n)]

def time_test1(n, runs):
    total1 = 0
    for _ in range(runs):
        L = create_random_list(n)
        heap1 = Heap(L)
        start = timeit.default_timer()
        heap1.build_heap1()
        total1 += timeit.default_timer() - start
    runtime1 = total1 / runs
    return runtime1

def time_test2(n, runs):
    total2 = 0
    for _ in range(runs):
        L = create_random_list(n)
        heap1 = Heap(L)
        start = timeit.default_timer()
        heap1.build_heap2()
        total2 += timeit.default_timer() - start
    runtime2 = total2 / runs
    return runtime2

def time_test3(n, runs):
    total3 = 0
    for _ in range(runs):
        L = create_random_list(n)
        heap1 = Heap(L)
        start = timeit.default_timer()
        heap1.build_heap3()
        total3 += timeit.default_timer() - start
    runtime3 = total3 / runs
    return runtime3

<<<<<<< HEAD
def timetest2(runs, length, sort):
    total = 0
    for _ in range(runs):
        L = create_near_sorted_list(length, 0.2)
        start = timeit.default_timer()
        sort(L)
        end = timeit.default_timer()
        total += end - start
    return total / runs

    return runtime1, runtime2, runtime3
=======
for i in range(1, 1001):
    print(i, time_test1(i, 20), time_test2(i, 20), time_test3(i, 20) )
>>>>>>> ef3b7efe45302762b3c11346dad5e3512a80f9fa

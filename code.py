import timeit
import random 

def create_random_list(n):
    return [random.random() for _ in range(n)]

def time_test(n, runs):
    total1 = 0
    total2 = 0
    total3 = 0

    for _ in range(runs):
        L = create_random_list(n)
        heap1 = Heap(L)
        start = timeit.default_timer()
        heap1.build_heap1()
        total1 += timeit.default_timer() - start
    runtime1 = total1 / runs

    for _ in range(runs):
        L = create_random_list(n)
        heap1 = Heap(L)
        start = timeit.default_timer()
        heap1.build_heap2()
        total2 += timeit.default_timer() - start
    runtime2 = total2 / runs

    for _ in range(runs):
        L = create_random_list(n)
        heap1 = Heap(L)
        start = timeit.default_timer()
        heap1.build_heap3()
        total3 += timeit.default_timer() - start
    runtime3 = total3 / runs

    return runtime1, runtime2, runtime3

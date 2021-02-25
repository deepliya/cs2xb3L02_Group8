from sorts import *

#Timetesting Section
def timetest(runs, length, sort):
    total = 0
    for _ in range(runs):
        L = create_random_list(length)
        start = timeit.default_timer()
        sort(L)
        end = timeit.default_timer()
        total += end - start
    return total / runs

def timetest_worstcase(runs, length, sort):
    total = 0
    for _ in range(runs):
        L = create_near_sorted_list(length, 0.001)
        start = timeit.default_timer()
        sort(L)
        end = timeit.default_timer()
        total += end - start
    return total / runs

def timetest_nearsorted(factor, sort):

    L = create_near_sorted_list(1000, factor)
    start = timeit.default_timer()
    selection_sort(L)
    end = timeit.default_timer()
    return end - start

def timetest2(runs, length, sort):
    total = 0
    for _ in range(runs):
        L = create_near_sorted_list(length, 0.2)
        start = timeit.default_timer()
        sort(L)
        end = timeit.default_timer()
        total += end - start
    return total / runs

for i in range(100, 10000, 100):
    print(i, timetest2(50, i, final_sort))

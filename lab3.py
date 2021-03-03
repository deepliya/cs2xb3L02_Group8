import random
import math
import timeit

def my_quicksort(L):
    copy = quicksort_copy(L)
    for i in range(len(L)):
        L[i] = copy[i]


def quicksort_copy(L):
    if len(L) < 2:
        return L
    pivot = L[0]
    left, right = [], []
    for num in L[1:]:
        if num < pivot:
            left.append(num)
        else:
            right.append(num)
    return quicksort_copy(left) + [pivot] + quicksort_copy(right)


def create_random_list(n):
    L = []
    for _ in range(n):
        L.append(random.randint(1,n))
    return L


def create_near_sorted_list(n, factor):
    L = create_random_list(n)
    L.sort()
    for _ in range(math.ceil(n*factor)):
        index1 = random.randint(0, n-1)
        index2 = random.randint(0, n-1)
        L[index1], L[index2] = L[index2], L[index1]
    return L

def dual_pivot_quicksort(L):
    if len(L) < 2:
        return L

    #put the pivots in ascending order
    if L[0] > L[-1]:
        L[0], L[-1] = L[-1], L[0]

    pivot1 = L[0]
    pivot2 = L[-1]
    left, right, center = [], [], []

    for num in L[1:-1]:
        if num <= pivot1:
            left.append(num)
        elif pivot1 < num < pivot2:
            center.append(num)
        else:
            right.append(num)
    return dual_pivot_quicksort(left) + [pivot1] + dual_pivot_quicksort(center) + [pivot2] + dual_pivot_quicksort(right)

for n in range(0, 200 + 1):

    list = create_random_list(n)
    print(timeit.timeit('%s' % dual_pivot_quicksort(list)))

import random
import timeit
import math

#Sorting Functions
def bubble_sort(L):
    for i in range(len(L)):
        swaps = 0
        for j in range(len(L) - 1 - i):
            if L[j] > L[j + 1]:
                swap(L, j, j + 1)
                swaps += 1
        if swaps == 0:
            return L


def swap(L, i, j):
    temp = L[i]
    L[i] = L[j]
    L[j] = temp


def insertion_sort(L):
    for i in range(1, len(L)):
        insert_into(L, i)
    return L


def insert_into(L, n):
    i = n
    while i > 0:
        if L[i] < L[i - 1]:
            swap(L, i, i-1)
        else:
            return
        i -= 1

def selection_sort(L):
    for i in range(len(L)):
        mindex = find_min_index(L, i)
        swap(L, i, mindex)
    return L


def find_min_index(L, n):
    mindex = n
    for i in range(n + 1, len(L)):
        if L[i] < L[mindex]:
            mindex = i
    return mindex

def final_sort(L):

    if (len(L) < 7):

        return insertion_sort(L)

    else:

        return dual_pivot_quicksort(L)

#Quicksort functions
def quicksort_inplace(L):
    def partition(L,left,right):
        if right-left<1: 
            return
        pivot = L[right]
        p = left
        for i in range(left, right):
            if L[i] < pivot:
                L[i],L[p] = L[p],L[i]
                p+=1
        L[p],L[right]=L[right],L[p]
        partition(L,left,p-1)
        partition(L,p+1,right)
    left = 0
    right = len(L)-1
    partition(L, left, right)
    return (L)

def our_quicksorts(L):
    copy = dual_pivot_quicksort(L)
    copy2 = tri_pivot_quicksort(L)
    print(copy, copy2)


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

def tri_pivot_quicksort(L):
    mid = len(L)//2

    if len(L) < 2:
        return L
    elif len(L) == 2:
        if L[1] < L[0]:
            L[0], L[1] = L[1], L[0]
        return L

    #put pivots in ascending order
    if L[0] <= L[-1] <= L[mid]:
        L[mid], L[-1] = L[-1], L[mid]
    elif L[mid] <= L[-1] <= L[0]:
        L[0], L[mid], L[-1] = L[mid], L[-1], L[0]
    elif L[mid] <= L[0] <= L[-1]:
        L[0], L[mid] = L[mid], L[0]
    elif L[-1] <= L[mid] <= L[0]:
        L[0], L[mid], L[-1] = L[-1], L[mid], L[0]
    elif L[-1] <= L[0] <= L[mid]:
        L[0], L[mid], L[-1] = L[-1], L[0], L[mid]

    pivot1 = L[0]
    pivot2 = L[mid]
    pivot3 = L[-1]
    left, left_center, right_center, right = [], [], [], []

    for i in range(1, len(L)-1):
        if i == mid:
            continue
        elif L[i] <= pivot1:
            left.append(L[i])
        elif pivot1 < L[i] <= pivot2:
            left_center.append(L[i])
        elif pivot2 < L[i] <= pivot3:
            right_center.append(L[i])
        else:
            right.append(L[i])
    return tri_pivot_quicksort(left) + [pivot1] + tri_pivot_quicksort(left_center) + \
           [pivot2] + tri_pivot_quicksort(right_center) + [pivot3] + tri_pivot_quicksort(right)

def quad_pivot_quicksort(L):
    mid1 = len(L) // 3
    mid2 = mid1 * 2

    if len(L) < 2:
        return L
    elif len(L) == 2:
        if L[1] < L[0]:
            L[0], L[1] = L[1], L[0]
        return L
    elif len(L) == 3:
        L = tri_pivot_quicksort(L)
        return L

    pivots_lst = [L[0], L[mid1], L[mid2], L[-1]]

    # put pivots in ascending order
    new_pivots_lst = tri_pivot_quicksort(pivots_lst)

    pivot1 = new_pivots_lst[0]
    pivot2 = new_pivots_lst[1]
    pivot3 = new_pivots_lst[2]
    pivot4 = new_pivots_lst[3]
    left, left_center, center, right_center, right = [], [], [], [], []

    for i in range(1, len(L) - 1):
        if i == mid1 or i == mid2:
            continue
        elif L[i] <= pivot1:
            left.append(L[i])
        elif pivot1 < L[i] <= pivot2:
            left_center.append(L[i])
        elif pivot2 < L[i] <= pivot3:
            center.append(L[i])
        elif pivot3 < L[i] <= pivot4:
            right_center.append(L[i])
        else:
            right.append(L[i])
    return quad_pivot_quicksort(left) + [pivot1] + quad_pivot_quicksort(left_center) + \
           [pivot2] + quad_pivot_quicksort(center) + [pivot3] + quad_pivot_quicksort(right_center) \
           + [pivot4] + quad_pivot_quicksort(right)

def final_sort(L):
    if len(L) < 6:
        insertion_sort(L)

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

#List Creation Section
def create_random_list(n):
    L = []
    for _ in range(n):
        L.append(random.randint(1, n))
    return L


def create_near_sorted_list(n, factor):
    L = create_random_list(n)
    L.sort()
    for _ in range(math.ceil(n*factor)):
        index1 = random.randint(0, n-1)
        index2 = random.randint(0, n-1)
        L[index1], L[index2] = L[index2], L[index1]
    return L

import random

def quicksort_inplace(lst):
	#should take a list as input and sort it without creating copies or other temporary lists

def our_quicksorts(L):
    copy = dual_pivot_quicksort(L)
    for i in range(len(L)):
        L[i] = copy[i]
    print(L)


def dual_pivot_quicksort(L):
    if len(L) < 2:
        return L
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

def tri_pivot_quicksort(lst):

def quad_pivot_quicksort(lst):

import random

def quicksort_inplace(lst):
	#should take a list as input and sort it without creating copies or other temporary lists

def our_quicksorts(L):
    copy = dual_pivot_quicksort(L)
    copy2 = tri_pivot_quicksort(L)
    print(copy, copy2)


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
def tri_pivot_quicksort(L):
    mid = len(L)//2
    if len(L) <= 2:
        return L
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
    for num in L[1:-1]:
        if num == pivot2:
            continue
        elif num <= pivot1:
            left.append(num)
        elif pivot1 < num <= pivot2:
            left_center.append(num)
        elif pivot2 < num <= pivot3:
            right_center.append(num)
        else:
            right.append(num)
    return tri_pivot_quicksort(left) + [pivot1] + tri_pivot_quicksort(left_center) + \
           [pivot2] + tri_pivot_quicksort(right_center) + [pivot3] + tri_pivot_quicksort(right)

def quad_pivot_quicksort(lst):

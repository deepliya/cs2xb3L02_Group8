import random

def quicksort_inplace(L):
    def sort(L,left,right):
        if right-left<1: 
            return
        pivot = L[right]
        p = left
        for i in range(left, right):
            if L[i] < pivot:
                L[i],L[p] = L[p],L[i]
                p+=1
        L[p],L[right]=L[right],L[p]
        sort(L,left,p-1)
        sort(L,p+1,right)
    l = 0
    r = len(L)-1
    sort(L, l, r)
    return (L)


quicksort_inplace(sample)

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


#def dual_pivot_quicksort(lst):

#def tri_pivot_quicksort(lst):

#def quad_pivot_quicksort(lst):

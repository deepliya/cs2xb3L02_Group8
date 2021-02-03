def quicksort_inplace(lst):

    if len(lst) < 2:
        return lst

    pivot = lst[len(lst) - 1]
    print(pivot)

    n = 0

    print(id(lst[n]))
    print(id(pivot))

    while id(lst[n]) != id(pivot):

        print(lst[n])

        if lst[n] > pivot:

            lst.append(lst.pop(n))
            print("qq")

        else:
            print("NAH")
            n+=1

    return lst

sample = [5, 10, 56, 1000, 56, 56, 0, -111111, 29, -29, 10]

print(quicksort_inplace(sample))

#def dual_pivot_quicksort(lst):

#def tri_pivot_quicksort(lst):

#def quad_pivot_quicksort(lst):

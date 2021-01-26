import timeit


def copy_function_1():
    lst = [1, 2, 3]
    copied_lst = lst.copy()
    return copied_lst


def copy_function_2():
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    copied_lst = lst.copy()
    return copied_lst


print(timeit.timeit(copy_function_1))
print(timeit.timeit(copy_function_2))


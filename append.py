import timeit

def million_list():
    lst = []
    for i in range(1000000):
        lst.append(i)
    return lst

print(timeit.timeit(million_list))

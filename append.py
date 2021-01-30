import timeit

lst = []
for i in range(0, 1000):
        print(timeit.timeit('%s' % lst.append(i)))

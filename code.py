
import timeit
import random

# CS/SE 2XB3 Lab 02 - Group 8 
# Chris, Deep, Victor

# Copy
def copy_function(lst):
    return lst.copy()

for i in range(0, 1001, 50):

    lst = [random.randint(1, 10) for iter in range(i)]
    print(len(lst), timeit.timeit('%s'%copy_function(lst)))
    

# Lookup
RandomListOfIntegers = [random.randint(1, 10) for iter in range(100001)]

def look_up(value):
    return RandomListOfIntegers[value]

for i in range (0, 100001):
    print (i, timeit.timeit('%s'%look_up(i)))
    
# Append
lst = []
for i in range(0, 1000000):
    if (i % 1000 == 0 or i == 999999):
        print(timeit.timeit('%s' % lst.append(i)))
    else:
        lst.append(i)
        
# Append Redesigned
for i in range(0, 1000):
        print(timeit.timeit('%s' % lst.append(i)))

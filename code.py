from graphs import *
import random 

#Testing Functions

def cycle_test(n, e):
    g = Graph(n)
    for i in range(e):
        nodes = random.sample(range(0, n), 2)
        g.add_edge(nodes[0], nodes[1])
    return has_cycle(g)

def is_connected_test(n, e):
    g = Graph(n)
    for i in range(e):
        nodes = random.sample(range(0, n), 2)
        g.add_edge(nodes[0], nodes[1])
    return is_connected(g)

def test1():
    n = 100
    for c in range (200):
        counter = 0
        for i in range(50):
            if cycle_test(n, c):
                counter += 1
        print(c, counter)

def test2():
    n = 100
    for c in range (500):
        counter = 0
        for i in range(20):
            if is_connected_test(n, c):
                counter += 1
        print(c, counter)

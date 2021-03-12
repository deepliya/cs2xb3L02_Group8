from graphs import *
import random 

#Testing functions
def cycle_test(n, e):
    g = Graph(n + 1)
    for i in range (1, e + 1):
        nodes = random.sample(range(1, 101), 2)
        g.add_edge(nodes[0], nodes[1])
    print(has_cycle(g))
    return has_cycle(g)

def is_connected_test(n, e):
    g = Graph(n + 1)
    for i in range (1, e + 1):
        nodes = random.sample(range(1, 101), 2)
        g.add_edge(nodes[0], nodes[1])
    print(is_connected(g))
    return is_connected(g)

is_connected_test(100, 30)

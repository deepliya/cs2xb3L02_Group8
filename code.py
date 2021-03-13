from graphs import *
import random 

#Testing Functions
def is_connected_test(n, e):
    g = Graph(n)
    for i in range(e):
        nodes = random.sample(range(0, n), 2)
        g.add_edge(nodes[0], nodes[1])
    return is_connected(g)

def test2():
    n = 100
    for c in range (500):
        for i in range(50):
            print(is_connected_test(n, c), c)

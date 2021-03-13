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
        counter = 0
        for i in range(50):
            if is_connected_test(n,c):
                counter += 1
        print(counter, " ", c)

test2()
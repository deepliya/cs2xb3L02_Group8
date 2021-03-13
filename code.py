from graphs import *
import random 

#Testing Functions
def cycle_test(n, e):
    g = Graph(n)
    for i in range(e):
        nodes = random.sample(range(0, n), 2)
        g.add_edge(nodes[0], nodes[1])
    print(has_cycle(g))
    return has_cycle(g)

def is_connected_test(n, e):
    g = Graph(n)
    for i in range(e):
        nodes = random.sample(range(0, n), 2)
        g.add_edge(nodes[0], nodes[1])
    print(is_connected(g))
    return is_connected(g)

def cycle_test2(runs, k, c):

    for i in range(c):

        counter = 0

        for j in range(runs):

            G = Graph(k)

            nodes = random.sample(range(0, k), 2)
            G.add_edge(nodes[0], nodes[1])

            if has_cycle(G):

                counter = counter + 1
        print(counter, " ", i)

def connected_test2(runs, k, c):

    for i in range(c):

        counter = 0

        for j in range(runs):

            G = Graph(k)

            nodes = random.sample(range(0, k), 2)
            G.add_edge(nodes[0], nodes[1])

            if is_connected(G):

                counter = counter + 1

        print(counter, " ", i)


def connected_test3(runs, k, c):
    for i in range(c):

        counter = 0

        for j in range(runs):

            G = Graph(k)

            for b in range(c):

                nodes = random.sample(range(0, k), 2)
                G.add_edge(nodes[0], nodes[1])

            if is_connected(G):
                counter = counter + 1

        print(counter, " ", i)

connected_test2(100, 100, 5000)
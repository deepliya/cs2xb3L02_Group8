import random
from shortest_paths import *
import timeit

def runtime_test(k):

    for i in range(1, k+1):

        G = create_random_complete_graph(100, 1000)
        start1 = timeit.default_timer()
        bellman_ford(G, 0)
        end1 = timeit.default_timer()

        start = timeit.default_timer()
        bellman_ford_approx(G, 0, i)
        end = timeit.default_timer()

        print(str(end1-start1) + " " + str(end - start))

def total_dist_test(k):

    for i in range(1, k+1):
        G = create_random_complete_graph(100, 1000)
        print(str(total_dist(bellman_ford_approx(G, 0, i))) + " " + str(total_dist(bellman_ford(G, 0))))


runtime_test(100)
total_dist_test(100)
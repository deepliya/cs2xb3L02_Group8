import random
from shortest_paths import *
import timeit

def runtime_test_approx(k):

    for i in range(1, k+1):

        G = create_random_complete_graph(100,1001)
        start = timeit.default_timer()
        bellman_ford_approx(G, 0, 1)
        end = timeit.default_timer()
        print(end-start)

def total_dist_test_approx(k):

    for i in range(1, k+1):
        G = create_random_complete_graph(100,1001)
        print(total_dist(bellman_ford_approx(G, 0, i)))





import random
import shortest_paths
import timeit

#Testing Functions


def runtime_test(function, k):

    if function == "bellman_ford":
        for i in range(k):
            G = create_random_complete_graph(101, 1000)
            start = timeit.default_timer()
            function(G,0)
            end = timeit.default_timer()
            print(end-start)
    else:
        for i in range(1, k + 1):
            G = create_random_complete_graph(101, 1000)
            start = timeit.default_timer()
            function(G, 0, k)
            end = timeit.default_timer()
            print(end-start)

def total_distance_test(function, k):

    if function == "bellman_ford":
        for i in range(k):
            G = create_random_complete_graph(101, 1000)
            print(yes)
    else:
        for i in range(1, k+1):
            G = create_random_complete_graph(101, 1000)
            print(total_dist(function(G, 0, k)))

total_distance_test("bellman_ford", 5)

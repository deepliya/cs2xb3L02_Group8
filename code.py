from lab8 import *
import random 

#weightedgraph from the lab picture
bigboy = WeightedGraph(10)
bigboy.add_edge(0, 1, 4)
bigboy.add_edge(0, 2, 3)
bigboy.add_edge(0, 9, 18)
bigboy.add_edge(0, 4, 10)
bigboy.add_edge(1, 2, 1)
bigboy.add_edge(1, 3, 4)
bigboy.add_edge(2, 4, 9)
bigboy.add_edge(2, 3, 5)
bigboy.add_edge(3, 4, 7)
bigboy.add_edge(3, 5, 9)
bigboy.add_edge(3, 6, 9)
bigboy.add_edge(4, 6, 8)
bigboy.add_edge(4, 7, 9)
bigboy.add_edge(4, 9, 8)
bigboy.add_edge(5, 6, 2)
bigboy.add_edge(5, 7, 4)
bigboy.add_edge(5, 8, 6)
bigboy.add_edge(6, 7, 2)
bigboy.add_edge(7, 8, 3)
bigboy.add_edge(7, 9, 9)
bigboy.add_edge(8, 9, 9)

g2 = WeightedGraph(5)
g2.add_edge(0, 1, 6)
g2.add_edge(0, 2, 11)
g2.add_edge(0, 3, 2)
g2.add_edge(1, 4, 3)
g2.add_edge(1, 2, 1)
g2.add_edge(2, 4, 3)
g2.add_edge(2, 3, 8)
g2.add_edge(3, 4, 10)

# def test1():
#     n = 100
#     for c in range (200):
#         counter = 0
#         for i in range(50):
#             if cycle_test(n, c):
#                 counter += 1
#         print(c, counter)

# def test2():
#     n = 100
#     for c in range (500):
#         counter = 0
#         for i in range(20):
#             if is_connected_test(n, c):
#                 counter += 1
#         print(c, counter)

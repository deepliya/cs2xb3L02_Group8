from collections import deque
import random

#Undirected graph using an adjacency list
class Graph:

    def __init__(self, n):
        self.adj = {}
        for i in range(n):
            self.adj[i] = []

    def are_connected(self, node1, node2):
        return node2 in self.adj[node1]

    def adjacent_nodes(self, node):
        return self.adj[node]

    def add_node(self):
        self.adj[len(self.adj)] = []

    def add_edge(self, node1, node2):
        if node1 not in self.adj[node2]:
            self.adj[node1].append(node2)
            self.adj[node2].append(node1)

    def number_of_nodes(self):
        return len(self.adj)

#Breadth First Search
def BFS(G, node1, node2):
    Q = deque([node1])
    marked = {node1 : True}
    for node in G.adj:
        if node != node1:
            marked[node] = False
    while len(Q) != 0:
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            if node == node2:
                return True
            if not marked[node]:
                Q.append(node)
                marked[node] = True
    return False


#Depth First Search
def DFS(G, node1, node2):
    S = [node1]
    marked = {}
    for node in G.adj:
        marked[node] = False
    while len(S) != 0:
        current_node = S.pop()
        if not marked[current_node]:
            marked[current_node] = True
            for node in G.adj[current_node]:
                if node == node2:
                    return True
                S.append(node)
    return False

#BFS2 & DFS2

def BFS2(G, node1, node2):
    Q = deque([node1])
    marked = {node1 : True}
    lst = []
    for node in G.adj:
        if node != node1:
            marked[node] = False
    while len(Q) != 0:
        current_node = Q.popleft()
        lst.append(current_node)
        for node in G.adj[current_node]:
            if node == node2:
                lst.append(node)
                return lst
            if not marked[node]:
                Q.append(node)
                marked[node] = True
    return []

def DFS2(G, node1, node2):
    S = [node1]
    marked = {}
    lst = []
    for node in G.adj:
        marked[node] = False
    while len(S) != 0:
        current_node = S.pop()
        lst.append(current_node)
        if not marked[current_node]:
            marked[current_node] = True
            for node in G.adj[current_node]:
                if node == node2:
                    lst.append(node)
                    return lst
                S.append(node)
    return []

#BFS3 & DFS3

def BFS3(G, node1):
    Q = deque([node1])
    marked = {node1 : True}
    pred = {}
    for node in G.adj:
        if node != node1:
            marked[node] = False
    while len(Q) != 0:
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            if node in pred or node == node1:
                continue
            if not marked[node]:
                Q.append(node)
                marked[node] = True
            pred[node] = current_node
    return pred

def DFS3(G, node1):
    S = [node1]
    marked = {}
    pred = {}
    for node in G.adj:
        marked[node] = False
    while len(S) != 0:
        current_node = S.pop()
        if not marked[current_node]:
            marked[current_node] = True
            for node in G.adj[current_node]:
                if node in pred or node == node1:
                    continue
                pred[node] = current_node
                S.append(node)
    return pred

def is_connected(G):
    checked = {}

    for node in G.adj:
        checked[node] = []

    for node1 in G.adj:
        for node2 in G.adj:
            if node2 not in checked[node1] and node1 not in checked[node2]:

                checked[node1].append(node2)
                checked[node2].append(node1)

                if not BFS(G, node1, node2):
                    return False

    return True

def node_cycle_check(G, node1):
    S = [node1]
    prev = [-1]
    marked = {}
    lst = []
    for node in G.adj:
        if len(G.adj[node]) == 1:
            marked[node] = True
        else:
            marked[node] = False
    while len(S) != 0:
        current_node = S.pop()
        prev.insert(0, current_node)
        parent = prev.pop()
        if not marked[current_node]:
            lst.append(current_node)
            marked[current_node] = True
            for node in G.adj[current_node]:
                if node == parent or (node in lst and node != node1):
                    continue
                if node == node1:
                    lst.append(node)
                    return True
                S.append(node)
    return False

def has_cycle(G):
    for i in range(G.number_of_nodes()):
        if node_cycle_check(G, i) is True:
            return True
    return False

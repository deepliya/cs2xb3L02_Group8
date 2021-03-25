import min_heap
import random

class DirectedWeightedGraph:

    def __init__(self):
        self.adj = {}
        self.weights = {}

    def are_connected(self, node1, node2):
        for neighbour in self.adj[node1]:
            if neighbour == node2:
                return True
        return False

    def adjacent_nodes(self, node):
        return self.adj[node]

    def add_node(self, node):
        self.adj[node] = []

    def add_edge(self, node1, node2, weight):
        if node2 not in self.adj[node2]:
            self.adj[node1].append(node2)
        self.weights[(node1, node2)] = weight

    def w(self, node1, node2):
        if self.are_connected(node1, node2):
            return self.weights[(node1, node2)]

    def number_of_nodes(self):
        return len(self.adj)


def dijkstra(G, source):
    pred = {} #Predecessor dictionary. Isn't returned, but here for your understanding
    dist = {} #Distance dictionary
    Q = min_heap.MinHeap([])
    nodes = list(G.adj.keys())

    #Initialize priority queue/heap and distances
    for node in nodes:
        Q.insert(min_heap.Element(node, 99999))
        dist[node] = 99999
    Q.decrease_key(source, 0)

    #Meat of the algorithm
    while not Q.is_empty():
        current_element = Q.extract_min()
        current_node = current_element.value
        dist[current_node] = current_element.key
        for neighbour in G.adj[current_node]:
            if dist[current_node] + G.w(current_node, neighbour) < dist[neighbour]:
                Q.decrease_key(neighbour, dist[current_node] + G.w(current_node, neighbour))
                dist[neighbour] = dist[current_node] + G.w(current_node, neighbour)
                pred[neighbour] = current_node
    return dist

def bellman_ford(G, source):
    pred = {} #Predecessor dictionary. Isn't returned, but here for your understanding
    dist = {} #Distance dictionary
    nodes = list(G.adj.keys())

    #Initialize distances
    for node in nodes:
        dist[node] = 99999
    dist[source] = 0

    #Meat of the algorithm
    for _ in range(G.number_of_nodes()):
        for node in nodes:
            for neighbour in G.adj[node]:
                if dist[neighbour] > dist[node] + G.w(node, neighbour):
                    dist[neighbour] = dist[node] + G.w(node, neighbour)
                    pred[neighbour] = node
    return dist

#bellman_ford_approx

def bellman_ford_approx(G, source, k):


    dist = {} # Distance dictionary
    k_track = {} # Dictionary to keep track of how many times distance was updated
    nodes = list(G.adj.keys()) # List of nodes from input graph

    # Initialize all distances to be infinity (99999)
    for node in nodes:
        dist[node] = 99999
        k_track[node] = 0
    dist[source] = 0

    for _ in range(G.number_of_nodes()):
        for node in nodes:
            for neighbour in G.adj[node]:
                if dist[neighbour] > dist[node] + G.w(node, neighbour) and k_track[neighbour] < k:
                    dist[neighbour] = dist[node] + G.w(node, neighbour)
                    k_track[neighbour] += 1

    return dist

#All pairs shortest paths

def all_pairs_dijkstra(G):
    matrix = []
    for i in (G.adj):
        dict1 = dijkstra(G, i)
        values = list(dict1.values())
        matrix.insert(i, values) 
    return matrix

def all_pairs_bellman_ford(G):
    matrix = []
    for i in (G.adj):
        dict1 = bellman_ford(G, i)
        values = list(dict1.values())
        matrix.insert(i, values) 
    return matrix


def total_dist(dist):
    total = 0
    for key in dist.keys():
        total += dist[key]
    return total

def create_random_complete_graph(n,upper):
    G = DirectedWeightedGraph()
    for i in range(n):
        G.add_node(i)
    for i in range(n):
        for j in range(n):
            if i != j:
                G.add_edge(i,j,random.randint(1,upper))
    return G


#Assumes G represents its node as integers 0,1,...,(n-1)
def mystery(G):
    n = G.number_of_nodes()
    d = init_d(G)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][j] > d[i][k] + d[k][j]:
                    d[i][j] = d[i][k] + d[k][j]
    return d

def init_d(G):
    n = G.number_of_nodes()
    d = [[999999 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if G.are_connected(i,j):
                d[i][j] = G.w(i,j)
        d[i][i] = 0
    return d

short = DirectedWeightedGraph()

short.add_node("A")
short.add_node("B")
short.add_node("C")
short.add_node("D")
short.add_node("E")
short.add_node("F")

short.add_edge("A", "B", 2)
short.add_edge("A", "C", 4)
short.add_edge("C", "E", 3)
short.add_edge("B", "C", 1)
short.add_edge("B", "D", 4)
short.add_edge("B", "E", 2)
short.add_edge("E", "D", 3)
short.add_edge("D", "F", 2)
short.add_edge("E", "F", 2)

a = DirectedWeightedGraph()

a.add_node(0)
a.add_node(1)
a.add_node(2)
a.add_node(3)
a.add_node(4)
a.add_node(5)
a.add_node(6)

a.add_edge(0, 1, 4)
a.add_edge(0, 6, 3)
a.add_edge(1, 2, 2)
a.add_edge(1, 3, 4)
a.add_edge(3, 5, 3)
a.add_edge(2, 3, 1)
a.add_edge(2, 4, 4)
a.add_edge(2, 5, 2)
a.add_edge(5, 4, 3)
a.add_edge(4, 6, 2)
a.add_edge(5, 6, 2)

"""print(dijkstra(a, 2))
print(bellman_ford(a, 2))

b = all_pairs_dijkstra(a)
print(b)
c = all_pairs_bellman_ford(a)
print(c)"""
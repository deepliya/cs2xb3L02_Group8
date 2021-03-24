from lab8 import *

def prim3(g):

    MST = WeightedGraph(g.number_of_nodes())
    L = []

    for i in range(g.number_of_nodes()):

        if i != 0:
            L.append(Element(99999,i))

    heap = MinHeap(L)

    for node in g.adjacent_nodes(0):

        






def prim2(g):

    MST = WeightedGraph(g.number_of_nodes())
    visited = []
    L = []

    for i in range(g.number_of_nodes()):
        if i == 0:
            L.append(0)
        else:
            L.append(99999)

    heap = MinHeap(L)

    while len(visited) != g.number_of_nodes():

        min_key = heap.extract_min.value

        while min_key in visited:

            min_key = heap.extract_min.value

        visited.append(min_key)

        for node in g.adjacent_nodes[min_key]:

            if g.w(min_key, node) < L[node]:
                heap.decrease_key(min_key, g.w(min_key, node))

        MST.add_edge(min_key,heap.get_min.value, g.w(min_key, heap.get_min.value))

    return MST

def prim1(g):

    global node2, node1, node_edge_combo
    MST = WeightedGraph(g.number_of_nodes())

    #Inital set A with two nodes and one edge
    A = [list(g.adj.keys())[0]]
    smallest_edge = g.adj[0][0][1]
    for i in g.adj[0]:
        if i[1] < smallest_edge:
            smallest_edge = i[1]
            A.append(i[0])
            MST.add_edge(i[0], list(g.adj.keys())[0], smallest_edge)
            g.adj[0].remove(i)
            for j in g.adj[i[0]]:
                if j[0] == 0:
                    g.adj[i[0]].remove(j)
                    break

    while len(A) < g.number_of_nodes():
        #iterate thru all the nodes in A
        smallest_edge = 1000
        for node in A:
            #find smallest edge of all that isn't connected to a node already in A
            #add the node to A
            #add edge to MST
            for i in g.adj[node]:
                if i[1] <= smallest_edge and i[0] not in A:
                    smallest_edge = i[1]
                    node_edge_combo = i
                    node2 = i[0]
                    node1 = node
        A.append(node2)
        MST.add_edge(node1, node2, smallest_edge)
        g.adj[node1].remove(node_edge_combo)
        for j in g.adj[node_edge_combo[0]]:
            if j[0] == node1:
                g.adj[node_edge_combo[0]].remove(j)
                break
                
    return MST.adj

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
print(prim2(bigboy))

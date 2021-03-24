from lab8 import *
import copy

def prim2(g):
    global node1
    MST = WeightedGraph(g.number_of_nodes())
    visited = [0]
    L = []

    for i in range(g.number_of_nodes()):
        L.append(Element(i, 99999))

    min_heap = MinHeap(L)
    i = 0

    while len(visited) < len(L):
        while i < len(visited):
            for j in g.adjacent_nodes(visited[i]):
                if j[0] in visited:
                    continue
                min_heap.decrease_key(j[0], j[1])
                if min_heap.get_min().value == j[0]:
                    node1 = visited[i]
            i += 1
        smallest_edge = min_heap.extract_min()
        MST.add_edge(node1, smallest_edge.value, smallest_edge.key)
        visited.append(smallest_edge.value)
        i = 0

    return MST.adj

def prim1(g):
    global node2, node1, node_edge_combo
    orig_graph = copy.deepcopy(g)
    MST = WeightedGraph(orig_graph.number_of_nodes())
    #Inital set A with two nodes and one edge
    A = [list(orig_graph.adj.keys())[0]]
    smallest_edge = orig_graph.adj[0][0][1]
    for i in orig_graph.adj[0]:
        if i[1] < smallest_edge:
            smallest_edge = i[1]
            A.append(i[0])
            MST.add_edge(i[0], list(orig_graph.adj.keys())[0], smallest_edge)
            orig_graph.adj[0].remove(i)
            for j in orig_graph.adj[i[0]]:
                if j[0] == 0:
                    orig_graph.adj[i[0]].remove(j)
                    break

    while len(A) < orig_graph.number_of_nodes():
        #iterate thru all the nodes in A
        smallest_edge = 1000
        for node in A:
            #find smallest edge of all that isn't connected to a node already in A
            #add the node to A
            #add edge to MST
            for i in orig_graph.adj[node]:
                if i[1] <= smallest_edge and i[0] not in A:
                    smallest_edge = i[1]
                    node_edge_combo = i
                    node2 = i[0]
                    node1 = node
        A.append(node2)
        MST.add_edge(node1, node2, smallest_edge)
        orig_graph.adj[node1].remove(node_edge_combo)
        for j in orig_graph.adj[node_edge_combo[0]]:
            if j[0] == node1:
                orig_graph.adj[node_edge_combo[0]].remove(j)
                break

    return MST.adj
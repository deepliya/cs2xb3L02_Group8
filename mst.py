from lab8 import *

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


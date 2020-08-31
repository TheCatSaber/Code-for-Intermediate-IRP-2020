"""Two methods of generating random graphs."""
#====Imports====#

import networkx as nx
import random

#====Helper Functions====#

def init_graph(size):
    """Make networkx.Graph() with size vertices.
    
    The vertices are unicode characters starting at 'A'."""
    graph = nx.Graph()
    # The ASCII reprensentation of 'A' is 65, 'B' is 66 etc.
    graph.add_nodes_from([chr(i) for i in range(65, 65+size)])
    return graph


#====Random Graph Functions====#

def random_graph(size, edge_number):
    """Create random graph, using method designed by the programmer.
    
    size -- size of random graph.
    edge_number -- number of edges per vertex.
    
    For each vertex, edge_number random edges are chosen,
    but the choice is discarded (without rechosing another edge)
    if the edge would form a loop or is already in the graph.
    """
    graph = init_graph(size)
    vertices = list(graph)
    for vertex in vertices:
        for counter in range(edge_number):
            # Choose a random vertex.
            vertex_choice = random.choice(vertices)
            if vertex_choice != vertex and vertex_choice not in graph[vertex]:
                graph.add_edge(vertex, vertex_choice)
    return graph

def erdos_renyi(size, p):
    """Create random graph, using the second Erdos-Renyi model.
    
    size -- size of random graph.
    p -- probability of each edge inclusion.

    Each possible edge in the graph is chosen with probability p
    Based on:
    https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93R%C3%A9nyi_model.
    """
    graph = init_graph(size)
    for vertex1 in graph:
        for vertex2 in graph:
            # Prevent trying each edge twice and loops.
            if vertex1 < vertex2:
                #random.random() returns a random number between 0 and 1.
                #So will be less than or equal to p with probability p.
                if p >= random.random():
                    graph.add_edge(vertex1, vertex2)
    return graph
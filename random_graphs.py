"""Two methods of generating random graphs."""
# Copyright (C) 2020 TheCatSaber

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

#====Imports====#

import networkx as nx
import random

#====Helper Functions====#

def init_graph(size):
    """Make networkx.Graph() with size vertices.
    
    The vertices are unicode characters starting at 'A'."""
    G = nx.Graph()
    # The ASCII reprensentation of 'A' is 65, 'B' is 66 etc.
    G.add_nodes_from([chr(i) for i in range(65, 65+size)])
    return G


#====Random Graph Functions====#

def random_graph(size, edge_number):
    """Create random graph, using method designed by the programmer.
    
    size -- size of random graph.
    edge_number -- number of edges per vertex.
    
    For each vertex, edge_number random edges are chosen,
    but the choice is discarded (without rechosing another edge)
    if the edge would form a loop or is already in the graph.
    """
    G = init_graph(size)
    vertices = list(G)
    for vertex in vertices:
        for counter in range(edge_number):
            # Choose a random vertex.
            vertex_choice = random.choice(vertices)
            if vertex_choice != vertex and vertex_choice not in G[vertex]:
                G.add_edge(vertex, vertex_choice)
    return G

def erdos_renyi(size, p):
    """Create random graph, using the second Erdos-Renyi model.
    
    size -- size of random graph.
    p -- probability of each edge inclusion.

    Each possible edge in the graph is chosen with probability p
    Based on:
    https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93R%C3%A9nyi_model.
    """
    G = init_graph(size)
    for vertex1 in G:
        for vertex2 in G:
            # Prevent trying each edge twice and loops.
            if vertex1 < vertex2:
                #random.random() returns a random number between 0 and 1.
                #So will be less than or equal to p with probability p.
                if p >= random.random():
                    G.add_edge(vertex1, vertex2)
    return G

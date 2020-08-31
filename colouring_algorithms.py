"""Greedy and DSatur colouring algorithms."""

#====Imports====#

from colouring_orders import degree_ordering, order_dict_return_list_reversed


#====Helper Functions====#

def smallest_available_colour(colour_list):
    """Returns the smallest colour that is not in colour_list."""
    colour = 0
    while True:
        if colour not in colour_list:
            return colour
        colour +=1

def neighbour_colours(vertex, graph, colouring):
    """Returns the set of neighbour colours of vertex.
    
    vertex -- the vertex to get the neighbours of.
    graph -- the graph.
    colouring -- the colouring to get the neighbour colours from."""
    neighbour_colours_list = [colouring[neighbour] for neighbour
        in graph[vertex] if neighbour in colouring]
    return set(neighbour_colours_list)


def saturation_degree_ordering(graph, colouring):
    """Return list of degree of saturation sorted descending,
    if the vertex is not already in the colouring.
    
    graph -- the graph in which to do this.
    colouring -- the colouring for which to do this.
    
    Degree of saturation = number of unique neighbour colours a
    vertex has.
    In case of ties, the one with the highest order is first,
    then the one highest in the alphabet.
    """
    # Dict containing number of neighbour colours for the colours
    # for the colours that are not in the colouring.
    # degree_ordering(graph) ensures that if there is a tie in
    # degree of saturation, the vertex woth the highest degree is
    # chosen first.
    saturation_degree_dict = {vertex: len(neighbour_colours(
        vertex, graph, colouring)) for vertex in degree_ordering(graph)
        if vertex not in colouring}
    # Convert to a list of the vertices, ordered in reverse by
    # the degree of saturation.
    sorted_ordering = order_dict_return_list_reversed(saturation_degree_dict)
    return sorted_ordering


#====Greedy Colouring====#

def greedy_colouring(graph, order):
    """Return dict colouring of graph by greedy algorithm.
    
    Goes through order and assigns first colour not used by vertex's
    neighbours to that vertex.
    Based on https://en.wikipedia.org/wiki/Greedy_coloring#Algorithm.
    """
    colouring = {}
    for vertex in order:
        # Colour is the smallest colour not in the neighbours' colours.
        colouring[vertex] = smallest_available_colour(
            neighbour_colours(vertex, graph, colouring))
    return colouring


#====DSatur====#

def dsatur_colouring(graph):
    """Return dict DSatur colouring of graph.
    
    See https://en.wikipedia.org/wiki/DSatur for how this works.
    Code based off the explanation from there and from 
    https://www.youtube.com/watch?v=L2csXWQMsNg?t=229.
    """
    colouring = {}
    for vertex_counter in range(len(graph.nodes())):
        sorted_saturation_degree = saturation_degree_ordering(graph, colouring)
        
        # vertex_to_colour is the vertex with the highest
        # degree of saturation (with ties broken by degree)
        vertex_to_colour = sorted_saturation_degree[0]
        neighbour_colours_of_vertex = neighbour_colours(
            vertex_to_colour, graph, colouring)
        
        # Colour is the smallest colour not in the neighbours' colours.
        colour = smallest_available_colour(neighbour_colours_of_vertex)
        colouring[vertex_to_colour] = colour
    return colouring

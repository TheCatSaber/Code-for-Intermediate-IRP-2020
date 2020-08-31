"""Create orders to run for greedy_colouring."""

#====Imports====#

import random


#====Helper Functions====#

def vertex_degrees(graph):
    """Return a dict in the form vertex: degree for graph."""
    vertex_degree_dict = {}
    for vertex in graph:
        vertex_degree_dict[vertex] = len(graph[vertex])
    return vertex_degree_dict


def order_dict_return_list_reversed(dictionary):
    """Return list of keys of dictionary, reversed,
    based on the value.
    """
    return [key for key, value in sorted(dictionary.items(),
            key=lambda item: item[1], reverse=True)]


#====Functions====#
def random_ordering(graph):
    """Create random shuffling of the vertices of graph."""
    vertices = list(graph)
    random.shuffle(vertices)
    return vertices

def degree_ordering(graph):
    """Make ordering for greedy_colouring for graph.
    This order has the highest degree vertex first, then the
    second highest degree vertex and so on.
    If there is a tie, it is done alphabetically.
    """
    vertex_degree_dict = vertex_degrees(graph)
    ordered_vertex_degrees = order_dict_return_list_reversed(
        vertex_degree_dict)
    return ordered_vertex_degrees
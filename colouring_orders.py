"""Create orders to run for greedy_colouring."""
# Copyright (C) 2020-21 TheCatSaber

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

import random


#====Helper Functions====#

def vertex_degrees(G):
    """Return a dict in the form vertex: degree for G."""
    vertex_degree_dict = {}
    for vertex in G:
        vertex_degree_dict[vertex] = len(G[vertex])
    return vertex_degree_dict

def order_dict_return_list(dictionary, reverse=False):
    """Return list of keys of dictionary,
    ordered on the value.
    
    dictionary -- dictionary to perform this to.
    reverse -- Whether to reverse the list. Value of reverse arguement
    in sorted().
    """
    return [key for key, value in sorted(dictionary.items(),
            key=lambda item: item[1], reverse=reverse)]

#====Functions====#
def random_ordering(G):
    """Create random shuffling of the vertices of G."""
    vertices = list(G)
    random.shuffle(vertices)
    return vertices

def degree_ordering(G):
    """Make ordering for greedy_colouring for G.
    
    This order has the highest degree vertex first, then the
    second highest degree vertex and so on.
    If there is a tie, it is done alphabetically.
    """
    vertex_degree_dict = vertex_degrees(G)
    ordered_vertex_degrees = order_dict_return_list(
        vertex_degree_dict, reverse=True)
    return ordered_vertex_degrees

"""Iterated Greedy colouring algorithm."""
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

import random
from colouring_algorithms import greedy_colouring, dsatur_colouring
from colouring_orders import (
    vertex_degrees, order_dict_return_list
)


#====Helper Functions====#

def create_groups(colouring):
    """Create colour groups for Iterated Greedy.
    
    colouring -- the colouring from which to make these groups.
    """
    groups_dict = {colour: [] for colour in colouring.values()}
    for vertex, colour in colouring.items():
        groups_dict[colour].append(vertex)
    groups_list = [vertex_list for vertex_list in groups_dict.values()]
    return groups_list

def one_d_list(two_d_list):
    """Create 1D list from 2D list.
    
    Goes through each list in two_d_list and appends
    the values to the one_d_list.    
    """
    one_d_list = []
    for list_ in two_d_list:
        for item in list_:
            one_d_list.append(item)
    return one_d_list

def total_degree(G, groups):
    """Find total degree in graph G of each group in groups."""
    degrees = vertex_degrees(G)
    total_degree_dict = {} #{vertex_list: 0 for vertex_list in groups}
    for counter in range(len(groups)):
        total_degree_dict[counter] = 0
        for vertex in groups[counter]:
            total_degree_dict[counter] += degrees[vertex]
    return total_degree_dict


def reverse_group_ordering(groups, G):
    """IG Ordering - reverse the groups (colour k first,
    then colour k-1 etc.).
    
    All IG Orderings contain G as an argument as some need it.
    This ensures the logic in iterated_greedy_colouring is easier.
    """
    order = one_d_list(groups)
    order.reverse()
    return order

def random_group_ordering(groups, G):
    """IG Ordering - random.
    
    All IG Orderings contain G as an argument as some need it.
    This ensures the logic in iterated_greedy_colouring is easier.
    """
    random.shuffle(groups)
    order = one_d_list(groups)
    return order

def largest_first_group_ordering(groups, G):
    """IG Ordering - largest size group first.
    
    All IG Orderings contain G as an argument as some need it.
    This ensures the logic in iterated_greedy_colouring is easier.
    """
    sorted_groups = sorted(groups, key=len)
    order = one_d_list(sorted_groups)
    return order

def smallest_first_group_ordering(groups, G):
    """IG Ordering - smallest size group first.
    
    All IG Orderings contain G as an argument as some need it.
    This ensures the logic in iterated_greedy_colouring is easier.
    """
    sorted_groups = sorted(groups, key=len, reverse=True)
    order = one_d_list(sorted_groups)
    return order

def increasing_total_degree_group_ordering(groups, G):
    """IG Ordering - increasing total degree of each group.
    
    All IG Orderings contain G as an argument as some need it.
    This ensures the logic in iterated_greedy_colouring is easier.
    """
    total_degree_dict = total_degree(G, groups)
    degree_ordered_colours = order_dict_return_list(total_degree_dict)
    degree_ordered_groups = [
        groups[colour] for colour in degree_ordered_colours
    ]
    order = one_d_list(groups)
    return order

def decreasing_total_degree_group_ordering(groups, G):
    """IG Ordering - decreasing total degree of each group.
    
    All IG Orderings contain G as an argument as some need it.
    This ensures the logic in iterated_greedy_colouring is easier.
    """
    total_degree_dict = total_degree(G, groups)
    degree_ordered_colours = order_dict_return_list(
    total_degree_dict, reverse=True)
    degree_ordered_groups = [
        groups[colour] for colour in degree_ordered_colours
    ]
    order = one_d_list(groups)
    return order

def get_ordering(ratios):
    """Return which IG Ordering to use, selected randomly,
    based on the ratios.
    """
    rand_int = random.randrange(sum(ratios.values()))
    if rand_int < ratios["reverse"]:
        return reverse_group_ordering
    elif rand_int < ratios["reverse"] + ratios["random"]:
        return random_group_ordering
    elif rand_int < ratios["reverse"] + ratios["random"] + ratios["largest"]:
        return largest_first_group_ordering
    elif rand_int < ratios["reverse"] + ratios["random"] + ratios["largest"] + ratios["smallest"]:
        return smallest_first_group_ordering
    elif rand_int < ratios["reverse"] + ratios["random"] + ratios["largest"] + ratios["smallest"] + ratios["increasing"]:
        return increasing_total_degree_group_ordering
    elif rand_int < ratios["reverse"] + ratios["random"] + ratios["largest"] + ratios["smallest"] + ratios["increasing"] + ratios["decreasing"]:
        return decreasing_total_degree_group_ordering
    else:
        print("An error occured.")
        return None

def iterated_greedy_colouring(G, inital_ordering, limit, goal_k, ratios={
        "reverse": 50,
        "random": 30,
        "largest": 50,
        "smallest": 0,
        "increasing": 0,
        "decreasing": 0
    }):
    """
    Inital ordering of class Colouring, or one of its children,
    must be run before iterated_greedy_colouring is called.
    """
    colouring = inital_ordering.colouring
    
    k = 0
    since_k_decreased = 0
    
    # k == 0 so inital k can be 0 so can enter while loop
    while since_k_decreased < limit and (k > goal_k or k==0):
        groups = create_groups(colouring)
        ordering_func = get_ordering(ratios)
        ordering = ordering_func(groups, G)
        colouring = greedy_colouring(G, ordering)
        
        k_new = len(set(colouring.values()))
        if k == k_new:
            since_k_decreased += 1
        else:
            since_k_decreased = 0
        
        k = k_new
    
    return colouring

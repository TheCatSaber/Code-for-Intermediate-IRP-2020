"""Classes to run multiple different colourings, once and many times."""
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

import time
import gc


#====List of Objects of this Class====#

colouring_object_list = []


#====Colouring Class====#

class Colouring:
    """A class to run multiple different colourings, once."""
    
    def __init__(self, name, colouring_function, config_name,
                 order_required=False, order_function=None,
                 preserve_capitalisation=False,
                 ig=False, ig_initial=None, ig_limit=None,
                 ig_goal_k=None, ig_ratios=None):
        """A class to run multiple different colourings, once.
        Call main_colouring_function with the graph you want to
        colour.
        
        name -- name.
        colouring_function -- the colouring function to call.
        Either with arguments (G) or (G, order) or (G, inital_ordering,
        limit, goal_k, ratios)
        config_name -- string used in graphs.config to specify
        which colouring should be displayed in the output.
        order_required -- True means the colouring function
        needs to be called with an order as the second arguement.
        order_function -- function to generate the order.
        preverse_capitalisation -- True keeps capitalisation of
        name the same for all output strings, otherwise follows
        normal capitalisation rules.
        ig -- whether the colouring is an iterated greedy.
        Iterated Greedy arguments are in the form ig_.
        ig_initial -- inital colouring to run for IG (either an object
        of the class Colouring or of the class of a child of Colouring)
        .
        ig_limit -- limit for IG.
        ig_goal_k -- goal_k for IG.
        ig_ratios -- ratios for IG.
        """
        self.name = name
        if preserve_capitalisation:
            self.name_start_sentence = name
            self.name_mid_sentence = name
        else:
            self.name_start_sentence = name.capitalize()
            self.name_mid_sentence = name.lower()
        self.colouring_function = colouring_function
        self.config_name = config_name
        self.order_required = order_required
        self.order_function = order_function
        colouring_object_list.append(self)
        self.ig = ig
        self.ig_initial = ig_initial
        self.ig_limit = ig_limit
        self.ig_goal_k = ig_goal_k
        self.ig_ratios = ig_ratios
    
    def run_colouring(self, G):
        """Run self.colouring_function on G,
        using the order from order_function if order_required.
        Return self.colouring (dict).
        """
        if self.order_required:
            self.order = self.order_function(G)
            self.colouring = self.colouring_function(G, self.order)
        elif self.ig:
            self.colouring = self.colouring_function(
                G, self.ig_initial, self.ig_limit, self.ig_goal_k)#,
                #self.ig_ratios)
        else:
            self.colouring = self.colouring_function(G)
        return self.colouring
    
    def time_colouring(self, G):
        """Time how long it takes to run self.run_colouring.
        Also disables garbage collection.
        """
        gc.disable()
        self.pre_colouring = time.time()
        self.run_colouring(G)
        self.post_colouring = time.time()
        gc.enable()
        self.colouring_duration = self.post_colouring - self.pre_colouring
        return self.colouring_duration
    
    def order_colouring(self):
        """Returns self.colouring ordered."""
        return {vertex:colour for vertex, colour in sorted(self.colouring.items())}

    def print_information(self):
        """Print information about the colouring of the graph."""
        # If an order was used, it prints the order and says
        # that the time for colouring included creating the order.
        self.order_text = ""
        if self.order_required:
            
            print(f"{self.name_start_sentence} order:")
            print(self.order)
            
            self.order_text = "(including creating the order) "
        
        # Outputs the colouring, along with how long it took,
        # and how many colours used.
        print(f"{self.name_start_sentence} colouring:")
        print(self.order_colouring())
        print(f"The {self.name_mid_sentence} colouring took " \
              f"{self.colouring_duration*1000:.3f} milliseconds " \
              f"{self.order_text}and used " \
              f"{len(set(self.colouring.values()))} colours.")
    
    def main_colouring_function(self, G):
        """Run self.time_colouring and print information if successful."""
        self.time_colouring(G)
        if self.colouring != None:
            self.print_information()


class ColouringRepeated(Colouring):
    """A class to run multiple different colourings, many times."""
    
    def __init__(self, name, colouring_function, config_name,
                 order_required=False, order_function=None,
                 preserve_capitalisation=False,
                 ig=False, ig_initial=None, ig_limit=None,
                 ig_goal_k=None, ig_ratios=None):
        """A class to run multiple different colourings, many times.
        
        name -- name.
        colouring_function -- the colouring function to call.
        Either with arguments (G) or (G, order) or (G, 
        config_name -- string used in graphs.config to specify
        which colouring should be displayed in the output.
        order_required -- True means the colouring function
        needs to be called with an order as the second arguement.
        order_function -- function to generate the order.
        preverse_capitalisation -- True keeps capitalisation of
        name the same for all output strings, otherwise follows
        normal capitalisation rules.
        ig -- whether the colouring is an iterated greedy.
        Iterated Greedy arguments are in the form ig_.
        ig_initial -- inital colouring to run for IG (either an object
        of the class Colouring or of the class of a child of Colouring)
        .
        ig_limit -- limit for IG.
        ig_goal_k -- goal_k for IG.
        ig_ratios -- ratios for IG.
        """
        self.total_colours = 0
        self.total_time = 0
        super().__init__(name, colouring_function, config_name, order_required,
                         order_function, preserve_capitalisation,
                         ig, ig_initial, ig_limit, ig_goal_k, ig_ratios)
        
    def print_information(self, times):
        """Print information about the colouring of the graph."""
        self.order_text = ""
        if self.order_required:
            self.order_text = " (including creating the orders)"
        
        print(f"The {times} {self.name_mid_sentence} colourings took " \
              f"{self.total_time:.6f} seconds{self.order_text} " \
              f"and used {self.total_colours} colours.")
    
    def main_colouring_function(self, G):
        """Time colouring, and add colours and time to
        total_colours and total_time.
        """
        self.time_colouring(G)
        self.total_colours += len(set(self.colouring.values()))
        self.total_time += self.colouring_duration
        
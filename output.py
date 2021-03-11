"""A way to ouput the coloured graph."""
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

import networkx as nx
import matplotlib.pyplot as plt


#====Constants====#

# Colours for use in output graph.
# Graphs that need more than 10 colours will just use 1 output colour.

OUTPUT_COLOURS = ["lightblue", "yellow", "lime", "red", "turquoise",
                  "magenta", "gold", "chocolate", "orange", "pink"]

#====Functions====#

def numerical_colouring_to_actual_colours(colouring):
    """Converts a numerical colouring to colours from OUTPUT_COLOURS."""
    output_colouring = []
    for vertex, colour in colouring.items():
        try:
            output_colouring.append(OUTPUT_COLOURS[colour])
        except IndexError:
            raise IndexError
    return output_colouring


def output_graph(G, colouring, show_labels):
    """Output G coloured with colouring and saves as graph.png.
    
    G -- graph to be output.
    colouring -- colouring to be output.
    show_labels -- boolean whether to show the labels on the output."""
    # Labels for the nodes
    labels = {vertex: vertex for vertex in G}
    
    # Colouring is None -> no output colouring
    if colouring == None:
        nx.draw_networkx(
            G, with_labels=show_labels, node_color="lightblue",
            linewidths=1.75, edgecolors="black", width=1.5, labels=labels,
            font_color="black")
    else:
        # Only convert into actual colours if colouring is not None
        try:
            colours_colouring = numerical_colouring_to_actual_colours(
                colouring)
        except IndexError:
            print("Too many colours to be displayed. " \
                  "Displaying with no colouring.")

            # Call this function with None as colouring
            output_graph(G, None, show_labels)
        except:
            print("Unexpected error in displaying colouring with colours, " \
                  "not using colours. " \
                  "Please make an issue on the GitHub page.")

            # Call this function with None as colouring
            output_graph(G, None, show_labels)

        nx.draw_networkx(
            G, with_labels=show_labels, node_color=colours_colouring,
            linewidths=1.75, edgecolors="black", width=1.5, labels=labels,
            font_color="black")
    
    plt.savefig("graph.png")
    plt.show()

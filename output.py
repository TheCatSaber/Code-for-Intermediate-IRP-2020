"""Way to ouput the coloured graph."""

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


def output_graph(graph, colouring, show_labels):
    """Output graph coloured with colouring and saves as graph.png.
    
    graph -- graph to be output.
    colouring -- colouring to be output.
    show_labels -- boolean whether to show the labels on the output."""
    # Labels for the nodes
    labels = {vertex: vertex for vertex in graph}
    
    # Colouring is None -> no output colouring
    if colouring == None:
        nx.draw_networkx(
            graph, with_labels=show_labels, node_color="lightblue",
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
            output_graph(graph, None, show_labels)
        except:
            print("Unexpected error in displaying colouring with colours, " \
                  "not using colours. " \
                  "Please make an issue on the GitHub page.")

            # Call this function with None as colouring
            output_graph(graph, None, show_labels)

        nx.draw_networkx(
            graph, with_labels=show_labels, node_color=colours_colouring,
            linewidths=1.75, edgecolors="black", width=1.5, labels=labels,
            font_color="black")
    
    plt.savefig("graph.png")
    plt.show()

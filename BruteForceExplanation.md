# This file explains how both brute force methods work.

# Shared functions explanation

## `colouring_list_to_dict(colouring_list, vertices)`
Turn a list of colours (`colouring_list`) and a list of vertices (`vertices`)
into a dictionary in the form vertex: colour.

```
def colouring_list_to_dict(colouring_list, vertices):
    colouring = {vertices[counter]: colouring_list[counter] for counter in range(len(colouring_list))}
    return colouring
```

## `validate_colouring(G, colouring)`
Return True if `colouring` is a valid colouring of G, False otherwise.

For edge, edge[0] is the start vertex, edge[1] is the end vertex.
Thus if they share a colour, it is an invalid colouring.

```
def validate_colouring(G, colouring):
    for edge in G.edges():
        if colouring[edge[0]] == colouring[edge[1]]:
            return False
    return True
```

# `product_brute_force_colouring(G)`

This works by generating all the combinations of `colours` colours for `size` vertices.
These are only tested if it contains colours-1 (the highest colour available),
to prevent repeated testing of previously done colourings.
`[i for i in range(colours)]` will produce a list of all the colours possible
for colours colours [0, 1, 2, ... colours-2, colours-1].

See explanation of [itertools.product](https://docs.python.org/3/library/itertools.html#itertools.product)
for details on what product does.

This runs in a while loop as will eventually find a colouring.
It starts with 1 colour, and then works up until it finds a valid colouring.

```
from itertools import product

def product_brute_force_colouring(G):
    size = len(G)
    vertices = list(G)
    colours = 1

    while True:
       colourings = product([i for i in range(colours)], repeat=size)
       for colouring_option in colourings:
          if colours - 1 in colouring_option:
              colouring = colouring_list_to_dict(colouring_option, vertices)
                  if validate_colouring(G, colouring):
                  return colouring
        colours += 1
```

# `custom_brute_force_colouring(G)`

Since `product_brute_force_colouring` tests equivalent colourings multiple times (e.g. 121 is equivalent to 212
as you can replace 1 with 2 and 2 with 1, TheCatSaber decided to create a custom brute force colouring method
that reduces repeated testings.

`vertices[0]` is always assigned the colour 0, `vertices[1]` is assigned either 0 or 1, `vertices[2]` is assigned either 0, 1 or 2 and so on.
However, no vertex can be assigned a colour greater than `colours`.
These colourings are only tested if they contain all the colours from 0 to `colours`,
otherwise it would be retesting a colouring that is equivalent to one already tested.

## `create_options(colours, size)`
Create a list with the number of colour options for each vertex.
It returns a list since the order isn't very important
It counts from 0 to colours (`options_0`). The other vertices then have colours options (`colours-1`).
`options_0` and `options_1` are then combined together and returned.
```
def create_options(colours, size):
    options_0 = [counter for counter in range(1, colours+1)]
    options_1 = [colours] * (size - len(options_0))
    full_options = options_0 + options_1
    return full_options
```

## `colouring_generator(colouring_index, options)`
Turn a for loop counter (`colouring_index`) into a list of colours for the graph.
This works equivalent to counting in a variable base system.
The algorithm starts at the end of `options` (by doing `for counter in range(len(options))-1, -1, -1):`;
counter will start at the last possible index for options, end at 0, counting down)
and finds the remainder of `colouring_index` divided by the number of options (`options[counter]`)
As `colouring_index` increases, this will go 0, 1, 2 ... `options[counter]-1` (which will be `colours-1`
(since the last possible colour is 1 less than colour)), and then back to 0, enumerating all of the options.
`colouring_index` is then set to `colouring index // options[counter]`
and then this is repeated for the next counter. This step effectively makes it the same as if the last vertex was not in the graph.

Colouring list is then reversed so the first vertex will always get colour 0.
```
def colouring_generator(colouring_index, options):
    colouring_list = []
    for counter in range(len(options)-1, -1, -1):
        colouring_list.append(colouring_index % options[counter])
        colouring_index = colouring_index // options[counter]
    colouring_list.reverse()
    return colouring_list
```

## `check_colours_items_in_colouring_list(colours, colouring_list)`
Check that there are colours unique items in colouring list.

```
def check_all_colours_in_colouring_list(colours, colouring_list):
    values = set(colouring_list)
    if len(set(colouring_list)) == colours:
        return True
    return False
```

## `custom_brute_force_colouring(G)`

The colouring will never require more colours than there are in G, so if colours is greater than size,
an error has occurred (and an error message is printed).

This runs in a while loop as will eventually find a colouring.
It starts with 1 colour, and then works up until it finds a valid colouring.

`number_colourings` is the number of colourings that need to be tested. This is just the product of all the items in the list.

```
def custom_brute_force_colouring(G):
    vertices = list(G)
    size = len(G)
    colours = 1

    while True:
        if colours <= size:
            try:
                options = create_options(colours, size)
            except:
                print("Error doing custom brute force colouring. " \
                      "Please make an issue on GitHub.")
                return None
        else:
            print("No custom brute force colouring found. " \
                  "Please make an issue on GitHub.")
            return None
        
        number_colourings = 1
        for option in options:
            number_colourings *= option
        
        for counter in range(number_colourings):
            colouring_list = colouring_generator(counter, options)
            if check_colours_items_in_colouring_list(colours, colouring_list):
                colouring = colouring_list_to_dict(colouring_list, vertices)
                if validate_colouring(G, colouring):
                    return colouring
        colours+=1
```

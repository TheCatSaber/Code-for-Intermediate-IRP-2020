# Code-for-Intermediate-IRP-2020
A collection of programs to colour graphs in various ways, once or many times, and to create random graphs.

Please check [License](https://github.com/TheCatSaber/Code-for-Intermediate-IRP-2020/#license)

# How to run the code
Install python 3.8 https://www.python.org/downloads/.

Click the code button, and click download zip.

Extract the code.

Install networkx with `pip install networkx` in the command line.

Install matplotlib with `pip install matplotlib` in the command line.

Set the values you want in graphs.config.

Run main.py (double click).

# Available Colourings

random_greedy: greedy colouring with a random order.

degree_greedy: greedy colouring with the highest degree vertex first,
then second highest degree and so on.

dsautr: DSatur colouring.

product_brute_force: brute force algorithm using itertools.product.

custom_brute_force: brute force algorithm designed by TheCatSaber.
The first vertex is always assigned the colour 0,
the second vertex the colours 0 or 1,
the third vertex the colours 0, 1 or 2 and so on.
However, the vertices have a maximum number of options of colours
(the number of colours currently being tested).
Colourings are only checked if they contain all the colours
from 0 to colours-1 (i.e. they have colours unique items).

# graphs.config file

Included is a graphs.config file which gives the default values.

graphSize (default: 6) - defines how many vertices in the graph.
Valid: any positive integer.

randomGraphEdgeNumber (default: 2) - number of edges per vertex for random_graphs().
Valid: any positive integer.

erdosRenyiP (default: 0.5) - defines p for Erdős-Rényi model. (The second one with G(n, p)).
Valid: any float. If value <= 0, there will be no edges, and if >= 1, the graph will be complete.

colouringToShow (default: None) - defines which colouring to show.
None is no colouring, others are the colouring of the same name.
Valid: None, randomGreedy, degreeGreedy, DSatur, productBruteForce, customBruteForce

showLabels (default: True) - whether to show the labels on the output graph. Boolean.

useErdosRenyi (default: True) - whether to use Erdős-Rényi for random graph generation.
If False, uses random_graphs() (designed by the progammer of these files). Boolean.

runBruteForce (default: True) - whether to run the brute force algorithms
(useful to make False if you want to run with large graphs). Boolean

timesToRun (default: 1) - If 1, run the run_once() function
(runs once and output includes a picture), if > 1,
run each colouring that number of times, but no picture output. Must be integer > 0.

# License

The code ("This program") is available under 
[GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html).
 
Copyright (C) 2020 TheCatSaber

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

The author should be stated as my real name if known, otherwise TheCatSaber.

# Sources
https://en.wikipedia.org/wiki/Greedy_coloring#Algorithm

https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93R%C3%A9nyi_model

https://www.python-course.eu/networkx.php

Aric A. Hagberg, Daniel A. Schult and Pieter J. Swart, “Exploring network structure, dynamics, and function using NetworkX”, in Proceedings of the 7th Python in Science Conference (SciPy2008), Gäel Varoquaux, Travis Vaught, and Jarrod Millman (Eds), (Pasadena, CA USA), pp. 11–15, Aug 2008

P. ERDŐS, A . RÉNYI, “On the Evolution of Random Graphs”, Institute of Mathematics, Hungarian Academy of Sciences, Hungary 5, 17-61, http://leonidzhukov.net/hse/2014/socialnetworks/papers/erdos-1960-10.pdf via google scholar

https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value

https://matplotlib.org/

https://networkx.github.io/documentation/latest/ 

https://docs.python.org/



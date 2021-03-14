# Code-for-Intermediate-IRP-2020
A collection of programs to colour graphs in various ways, once or many times,
to create random graphs and display a picture if run once (an example graph.png is included).

Please check [License](https://github.com/TheCatSaber/Code-for-Intermediate-IRP-2020#license) for information on reuse.

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

dsatur: DSatur colouring.

product_brute_force: brute force algorithm using itertools.product.

custom_brute_force: brute force algorithm designed by TheCatSaber.
For an explantion of both brute forces see
[BruteForceExplanation.md](https://github.com/TheCatSaber/Code-for-Intermediate-IRP-2020/blob/master/BruteForceExplanation.md)

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
Valid: None, randomGreedy, degreeGreedy, DSatur, productBruteForce, customBruteForce, iteratedGreedy.

showLabels (default: True) - whether to show the labels on the output graph. Must be a boolean.

useErdosRenyi (default: True) - whether to use Erdős-Rényi for random graph generation.
If False, uses random_graphs() (designed by TheCatSaber). Must be a boolean.

runBruteForce (default: True) - whether to run the brute force algorithms
(useful to make False if you want to run with large graphs). Must be a boolean.

timesToRun (default: 1) - If 1, run the run_once() function
(runs once and output includes a picture), if > 1,
run each colouring that number of times, but no picture output. Must be an integer > 0.

IGInital (default: "degree_greedy") - the initial colouring to use for iterated greedy.
Invalid will default to degree_greedy
Valid: degree_greedy, random_greedy, dsatur

IGLimit (default: 100) - how many iterations of iterated greedy to perform without decrease
in number of colours.
Valid: any positive integer.

IGGoalK (default: 1) - goal for how many colours to achieve in iterated greedy.
Iterated greedy will automatically stop once achieved.
Valid: any positive integer.

ig_ratios (default: 50,30,50,0,0,0) - Ratios for functions for iterated greedy.
In order: reverse group, random group, largest first group, smallest first group,
increasing total degree, decreasing total degree.
Valid: comma separated values of 6 positive integers (no spaces).

# License

The code ("This program") is available under 
[GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html).

A copy is included
[here](https://github.com/TheCatSaber/Figures-for-Intermediate-IRP-2020/blob/master/LICENSE).
 
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

https://en.wikipedia.org/wiki/DSatur

https://www.python-course.eu/networkx.php

Aric A. Hagberg, Daniel A. Schult and Pieter J. Swart, “Exploring network structure, dynamics, and function using NetworkX”, in Proceedings of the 7th Python in Science Conference (SciPy2008), Gäel Varoquaux, Travis Vaught, and Jarrod Millman (Eds), (Pasadena, CA USA), pp. 11–15, Aug 2008

Erdős, P., Rényi, A.  On Random Graphs. I. Publicationes Mathematicae, 6, pp. 290–297. https://www.renyi.hu/~p_erdos/1959-11.pdf .

Gilbert, E. N. Random Graphs. The Annals of Mathematical Statistics, vol. 30, no. 4, 1959, pp. 1141–1144. JSTOR, https://www.jstor.org/stable/2237458 .

https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value

https://matplotlib.org/

https://networkx.github.io/documentation/latest/ 

https://docs.python.org/

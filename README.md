# shortestpath
The code functions to find shortest path from source to destination via selection of best possible internal node path and visualize the path


modules used 
for gui tkinter
for plotting and visualizing graph matplotlib
for shortest path prediction networkx 

theory 
tkinter : Tkinter is the standard GUI library for Python. 
          Python when combined with Tkinter provides a fast and easy way to create GUI applications. 
          Tkinter provides a powerful object-oriented interface to the Tk GUI toolkit.

matplotlib : Matplotlib is one of the most popular Python packages used for data visualization. 
             It is a cross-platform library for making 2D plots from data in arrays.  
             It provides an object-oriented API that helps in embedding plots in applications using Python GUI toolkits such as PyQt, WxPythonotTkinter. 
             It can be used in Python and IPython shells, Jupyter notebook and web application servers also.

networkx : NetworkX is a Python language software package for the creation, manipulation, and study of the structure, dynamics, and functions of complex networks. 
           Pygraphviz is a Python interface to the Graphviz graph layout and visualization package.
           This is the main module which helps to calculate shortast path on the provided graph inputs
           
SHORTEST PATH 
In graph theory, the shortest path problem is the problem of finding a path between two vertices (or nodes) in a graph such that the sum of the weights of its constituent edges is minimized.
The problem of finding the shortest path between two intersections on a road map may be modeled as a special case of the shortest path problem in graphs, where the vertices correspond to intersections and the edges correspond to road segments, each weighted by the length of the segment.
The shortest path problem can be defined for graphs whether undirected, directed, or mixed. It is defined here for undirected graphs; for directed graphs the definition of path requires that consecutive vertices be connected by an appropriate directed edge.
The most important algorithms for solving this problem are:
  Dijkstra's algorithm solves the single-source shortest path problem with non-negative edge weight.
  Bellman–Ford algorithm solves the single-source problem if edge weights may be negative.
  A* search algorithm solves for single-pair shortest path using heuristics to try to speed up the search.
  Floyd–Warshall algorithm solves all pairs shortest paths.
  Johnson's algorithm solves all pairs shortest paths, and may be faster than Floyd–Warshall on sparse graphs.
  Viterbi algorithm solves the shortest stochastic path problem with an additional probabilistic weight on each node.
  
APPLICATIONS
Shortest path algorithms are applied to automatically find directions between physical locations, such as driving directions on web mapping websites like MapQuest or Google Maps. For this application fast specialized algorithms are available.

INPUT METHODS TO RUN THIS PROGRAM
format for inputs with an example
no of edges : 6    click next
fill the edge vertex details  
from   to  cost
  a     b   1    {after feilling each row please keep clicking the next button
  b     c   2       unless you get aytomatically get to next filling area}
  a     c   3
  c     d   4
  d     e   2
  b     e   1
 noe to find the shortast path between we need to fill the source and destination as
 source:a    destination: e {take according to your graph}
click calculate and it will show you the shortest path 
now click on visuaize to get the graph output
just clicking reset it will relaunch the default fresh program by killing the previous one
note if vany wrong input it shows a warning at the top left corner withn no of times the warning occured

JUST FOR REFERENCE GRAPH DESIGN TO UNDERSTAND INPUT FORMAT MORE CLEAR

            b -------1------e
           /  \            /
         1     2          2
        /        \       /
      a-----3-----c-----d
NOTE : THERE IS A BUG IN SYSTEM THE RESET BUTTON DOES NOT CLEAR THE PREVIOUS PLOTTED GRAPH SO TO RESET WE HAVE TO RESTART THE APPLIOCATION

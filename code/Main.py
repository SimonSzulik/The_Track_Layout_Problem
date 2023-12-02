"""
 * ************************
 *	Bachelor-Thesis Simon Szulik
 *
 *      The Track Layout Problem
 *      from a SAT-Solving Perspective
 *
 * ************************
"""

from Sat_Solving_TLP import compute_tlp
from Data_Script import get_dataset
import numpy as np
import sys

"""
 * ***** space for own example graphs ***** *
"""

nodes = 4
tracks = 3

# adjacency matrix
edges = [[0 for _ in range(nodes)] for _ in range(nodes)]

# complete graph
for i in range(nodes - 1):
    for j in range(i + 1, nodes):
        edges[i][j] = 0

# Edges for Test Graphs

edges[0][1] = 1
edges[1][0] = 1

edges[1][2] = 1
edges[2][1] = 1

edges[2][3] = 1
edges[3][2] = 1

"""
 * ***** dataset to analyze ***** *
"""

test_graphs = get_dataset('../Data_Sets/Data_Set_10*n_Nodes.txt')

"""
* get single graphs from dataset to analyze
* compute single graphs or own examples
"""

#for filename, matrix in test_graphs.items():
#    if filename == "grafo327.10.gml":
#        print(f"File: {filename}")
#        print("adjacency matrix:")
#        print(matrix)
#        edges = matrix
#        print("------")
#        compute_tlp(len(edges), edges, tracks, 2)

"""
 * ***** compute whole dataset ***** *
 * ***** !!! TO DO !!! ***** *
"""

for filename, matrix in test_graphs.items():
    # if name contains anzahl knoten
    # --> in file schreiben
    graph_class = filename.split('.')[1]
    path = '../results/' + graph_class + ".txt"
    track_counter = 1

    print(matrix)

    with open(path, 'w') as f:
        f.write(f"File: {filename}")
        f.write("\n")
        f.write("------------")
        f.write("\n")
        edges = matrix

        sys.stdout = f

        while not compute_tlp(len(edges), edges, track_counter, 2):
            track_counter += 1

        f.write("------------------------")
        f.write("\n")


#    print(f"File: {filename}")
#    print("adjacency matrix:")
#    print(matrix)
#    print("------")
#    edges = matrix
#
#    track_counter = 1
#
#    while not compute_tlp(len(edges), edges, track_counter, 2):
#        track_counter += 1



#while not compute_tlp(len(edges), edges, tracks, 2):
#    tracks += 1



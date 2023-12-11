"""
 * ************************
 *	Bachelor-Thesis Simon Szulik WS 2023/24
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
 * ***** space for own example graphs and its computation ***** *
"""

# nodes = 5
# tracks = 5

# adjacency matrix
# edges = [[0 for _ in range(nodes)] for _ in range(nodes)]

# complete graph
# for i in range(nodes - 1):
#    for j in range(i + 1, nodes):
#        edges[i][j] = 1

# Edges for Test Graphs

# edges[0][1] = 1
# edges[1][0] = 1

# edges[1][2] = 1
# edges[2][1] = 1

# edges[2][3] = 1
# edges[3][2] = 1

# compute_tlp(len(edges), edges, tracks, 2)

"""
 * ***** dataset to analyze ***** *
"""

test_graphs = get_dataset('../Data_Sets/Data_Set_10n_Nodes.txt')

"""
 * ***** compute whole dataset (small part of rome_gml ***** *
"""

for filename, matrix in test_graphs.items():
    method = "2"
    if "toDO" in filename:
        # graphen die länger dauern könnten, einzeln testen
        # check graphs for 80 nodes if they run longer than 12 hours and method 2
        # grafo4865.80.gml
        # grafo9795.80.gml
        # grafo7907.80.gml
        # check graphs for 90 nodes if they run longer than 12 hours and method 2
        # grafo7130.90.gml
        # grafo8558.90.gml
        # grafo8952.90.gml
        # grafo8946.90.gml
        # grafo3756.90.gml
        # check graphs for 10 nodes if they run longer than 12 hours and method 2

        graph_class = filename.split('.')[1]
        path = '../results/' + graph_class + "_" + method + ".txt"
        track_counter = 1
        original_stdout = sys.stdout

        print(filename, "is getting tested now")

        with open(path, 'a') as f:
            edges = matrix
            f.write(f"File: {filename} with {len(edges)} Nodes and {np.sum(matrix)/2} Edges")
            f.write("\n")
            f.write("------------")
            f.write("\n")

            sys.stdout = f

            while not compute_tlp(len(edges), edges, track_counter, 2):
                track_counter += 1

            f.write("\n")
            f.write("------------------------")
            f.write("\n")
            sys.stdout = original_stdout

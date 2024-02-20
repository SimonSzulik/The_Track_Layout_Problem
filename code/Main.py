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

nodes = 3
tracks = 3

# adjacency matrix
edges = [[0 for _ in range(nodes)] for _ in range(nodes)]

# complete graph
for i in range(nodes - 1):
    for j in range(i + 1, nodes):
        edges[i][j] = 1

# Edges for Test Graphs

edges[0][1] = 1
edges[1][0] = 1

edges[1][2] = 1
edges[2][1] = 1

edges[2][0] = 1
edges[0][2] = 1

compute_tlp(len(edges), edges, tracks, 2)

"""
 * ***** dataset to analyze ***** *
"""

test_graphs = get_dataset('../Data_Sets/Data_Set_10n_Nodes.txt')

"""
 * ***** compute dataset (small part of Rome-Lib) ***** *
"""

# for filename, matrix in test_graphs.items():
# vars for output // approach used
#    method = "3"
#    approach = 3

#    graph_class = filename.split('.')[1]
#    path = '../results/' + graph_class + "_" + method + ".txt"
#    track_counter = 1
#    original_stdout = sys.stdout

#    print(filename, "is getting tested now")

# search graph in Rome-Lib and test it
#    with open(path, 'a') as f:
#        edges = matrix
#        f.write(f"File: {filename} with {len(edges)} Nodes and {np.sum(matrix) / 2} Edges")
#        f.write("\n")
#        f.write("------------")
#        f.write("\n")

#        sys.stdout = f

# loop until Track-Layout was found / F(G,t) starting by t = 1
#        while not compute_tlp(len(edges), edges, track_counter, approach):
#            track_counter += 1

#        f.write("\n")
#        f.write("------------------------")
#        f.write("\n")
#        sys.stdout = original_stdout

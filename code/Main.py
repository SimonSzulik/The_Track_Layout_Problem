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

"""
 * ***** Space for own Example Graphs ***** *
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
 * ***** Dataset to analyze ***** *
"""

test_graphs = get_dataset('../Data_Sets/Data_Set_10*n_Nodes.txt')

"""
* get single graphs from dataset to analyze
* compute single graphs or own examples
"""

for filename, matrix in test_graphs.items():
    if filename == "grafo327.10.gml":
        print(f"File: {filename}")
        print("adjacency matrix:")
        print(matrix)
        edges = matrix
        print("------")

# method 1 = Approach 1
# method 2 = Approach 2
# method 3 = Approach 3 with ψ as improvements
# compute_tlp(len(edges), edges, tracks, 2)

"""
 * ***** compute whole dataset ***** *
 * ***** !!! TO DO !!! ***** *
"""

while not compute_tlp(len(edges), edges, tracks, 3):
    tracks += 1



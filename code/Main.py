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
 * ***** Space for Example Graphs ***** *
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
test_graphs = get_dataset()
print(test_graphs)
"""
* toDO:
* für jeden graphen methode ausführen anfangend von 1 track hoch bis es funktioniert
"""
#for filename, matrix in test_graphs.items():
 #   print(f"File: {filename}")
  #  print("adjacency matrix:")
   # print(matrix)
    #edges = matrix
    #print("------")

"""
 * ***** Compute ***** *
"""

#compute_tlp(len(edges), edges, tracks, 1)

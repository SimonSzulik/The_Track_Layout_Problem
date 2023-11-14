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

"""
 * ***** Space for Example Graphs ***** *
"""

nodes = 4
tracks = 2

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
 * ***** Compute ***** *
"""

compute_tlp(4, edges, tracks, 2)


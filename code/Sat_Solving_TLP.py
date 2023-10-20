"""
 * ************************
 *	Bachelor-Thesis Simon Szulik
 *
 *      The Track Layout Problem
 *      from a SAT-Solving Perspective
 *
 * ************************
"""

# imports
from pysat.solvers import Lingeling
from Node_Clause import get_node_clauses
from Sequence_Clause import get_sequence_clauses_relation, get_sequence_clauses_per_track

"""
 * ***** Beispielgraph ***** *
"""

nodes = 4
tracks = 4

# adjacency matrix
edges = [[0 for _ in range(nodes)] for _ in range(nodes)]

# complete graph
for i in range(nodes - 1):
    for j in range(i + 1, nodes):
        edges[i][j] = 1

# [1,2,3,4] ==> 1, if node 1 os on track 1 !
#           ==> 2, if node 1 is on track 2 !
# etc.
# ==> ( track * nodes ) variables
formula = get_node_clauses(nodes, tracks, edges)
#formula = get_sequence_clauses_per_track(nodes, tracks, edges)

with Lingeling(bootstrap_with=formula.clauses, with_proof=False) as ling:
    print(ling.solve())
    print(formula.clauses)
    print(ling.get_model())

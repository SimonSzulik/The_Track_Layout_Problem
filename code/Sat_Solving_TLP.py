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
import time
from Create_Formula import get_node_clauses, get_sequence_clauses_relation, get_sequence_total_order
from CustomSolver import CustomSolver
from String_Formatter import get_position, get_order

"""
 * ***** Space for Example Graphs ***** *
"""

nodes = 4
tracks = 4

# adjacency matrix
edges = [[0 for _ in range(nodes)] for _ in range(nodes)]

# complete graph
for i in range(nodes - 1):
    for j in range(i + 1, nodes):
        edges[i][j] = 1

"""
 * ***** Space for Example Graphs ***** *
"""

"""
 * ***** Collecting all Clauses and calculate with Lingeling ***** *
 --> Comment out the Methods needed and comment the others
"""
# For both methods
formula = get_node_clauses(nodes, tracks, edges)
# formula.extend(get_sequence_clauses_relation(nodes, tracks, edges))
formula.extend(get_sequence_total_order(nodes, tracks, edges))

"""
 * ***** Collecting all Clauses and calculate with Lingeling ***** *
"""

"""
 * ***** Compute Sat-Solving-Model if possible and print the Track-Layout-Configuration as text ***** *
  --> Comment out the Methods needed and comment the others
"""
start = time.time()

solver = CustomSolver()
solver.add(formula)
model = solver.get_model() if solver.solve() else []

end = time.time()

print("The Sat-Formula", model)
print("calculated to", solver.evaluate_formula(model), "in", end-start, "seconds.")
print(formula.clauses)

"""
 * ***** add "1/2" to get_order parameters to get the matching sequence/total_order output***** *
"""
get_position(model, nodes, tracks)
get_order(model[nodes*tracks:], nodes, tracks, 2)


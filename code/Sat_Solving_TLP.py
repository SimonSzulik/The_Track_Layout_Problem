"""
 * ************************
 *	Bachelor-Thesis Simon Szulik
 *
 *      The Track Layout Problem
 *      from a SAT-Solving Perspective
 *
 * ************************
"""
from pysat.formula import CNF
# imports
from pysat.solvers import Lingeling
from Create_Formula import get_node_clauses
from Create_Formula import get_sequence_clauses_relation
#from Sequence_Clause import get_sequence_clauses_relation, get_sequence_clauses_per_track
from CustomSolver import CustomSolver

"""
 * ***** Beispielgraph ***** *
"""

nodes = 4
tracks = 2

# adjacency matrix
edges = [[0 for _ in range(nodes)] for _ in range(nodes)]

# complete graph
for i in range(nodes - 1):
    for j in range(i + 1, nodes):
        edges[i][j] = 0

formula = get_node_clauses(nodes, tracks, edges)
formula_2 = get_sequence_clauses_relation(nodes, tracks, edges)

combined = CNF()

combined.extend(formula.clauses)
combined.extend(formula_2.clauses)

solver = CustomSolver()
solver.add(combined)
model = solver.get_model() if solver.solve() else []

print(model)
print(solver.evaluate_formula(model))
print(combined.clauses)

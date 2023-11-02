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
from Create_Formula import get_node_clauses
from Create_Formula import get_sequence_clauses_relation, get_sequence_total_order
from CustomSolver import CustomSolver

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

"""
 * ***** Beispielgraph ***** *
"""

"""
 * ***** Collecting all clauses and calculate with Lingeling ***** *
"""
formula = get_node_clauses(nodes, tracks, edges)
#formula.extend(get_sequence_clauses_relation(nodes, tracks, edges))
formula.extend(get_sequence_total_order(nodes, tracks, edges))
#formula = get_sequence_total_order(nodes, tracks, edges)

solver = CustomSolver()
solver.add(formula)
model = solver.get_model() if solver.solve() else []

print(model)
print(solver.evaluate_formula(model))
print(formula.clauses)

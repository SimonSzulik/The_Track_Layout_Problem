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
 * ***** F(G,t) ***** *
 * n = nodes, g = Graph as adjacency matrix, t = tracks, m = SAT-Method 1/2 = Relational Sequence/Total Order )
"""


def compute_tlp(nodes, graph, tracks, method):
    """
     * ***** Collecting all Clauses ***** *
    """
    formula = get_node_clauses(nodes, tracks, graph)
    if method == 1:
        formula.extend(get_sequence_clauses_relation(nodes, tracks, graph))
    elif method == 2:
        formula.extend(get_sequence_total_order(nodes, tracks, graph))
    else:
        print("wrong method")

    """
     * ***** Compute Sat-Solving-Model if possible ***** *
    """
    start = time.time()

    solver = CustomSolver()
    solver.add(formula)
    model = solver.get_model() if solver.solve() else []

    end = time.time()

    print("The Sat-Formula", model)
    print("calculated to", solver.evaluate_formula(model), "in", end - start, "seconds.")
#   print(formula.clauses)

    """
     * ***** Print TLP configuration as text ***** *
    """
    print("\n" "The TLP has the following configuration: \n")
    get_position(model, nodes, tracks)

    if method == 1:
        get_order(model[nodes * tracks:], nodes, tracks, 1)
    elif method == 2:
        get_order(model[nodes * tracks:], nodes, tracks, 2)
    else:
        print("wrong method")

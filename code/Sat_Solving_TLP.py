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
 * n = nodes, g = Graph as adjacency matrix, t = tracks, m = SAT-Method 1/2 = Relational Sequence/Total Order ) *
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
    print("The formula contained", len(formula.clauses), "clauses")

    """
     * ***** Print TLP configuration as text ***** *
    """
    print("\n" "The TLP has the following configuration: \n")
    track_list = get_position(model, nodes, tracks)
    #  print(track_list)

    if method == 1:
        longest_neighborlist = []
        order_list = get_order(model[nodes * tracks:], nodes, tracks, 1)
        for track_key in track_list:
            maximum = 0
            for node_value in track_list[track_key]:
                if len(order_list[node_value]) > maximum:
                    maximum = len(order_list[node_value])
                    longest_neighborlist.append(node_value)

        for track_order in longest_neighborlist:
            right_nodes = " ---- "
            for right_neighbor in order_list[track_order]:
                right_nodes += str(right_neighbor)
                right_nodes += " ---- "
            print("----", track_order, right_nodes)
    elif method == 2:
        get_order(model[nodes * tracks:], nodes, tracks, 2)
    else:
        print("wrong method")

    return solver.solve()

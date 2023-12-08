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
 * ***** F(G,t) ***** * * n = nodes, g = Graph as adjacency matrix, t = tracks
 * m = SAT-Method 1/2/3 = Total_Order/Relational_Sequence/Relational_Sequence_Improved 
"""


def compute_tlp(nodes, graph, tracks, method):
    """
     * ***** collecting all clauses ***** *
    """
    formula = get_node_clauses(nodes, tracks, graph)

    start = time.time()

    if method == 1:
        formula.extend(get_sequence_total_order(nodes, tracks, graph))
    elif method == 2:
        formula.extend(get_sequence_clauses_relation(nodes, tracks, graph, "Not_Improved"))
    elif method == 3:
        formula.extend(get_sequence_clauses_relation(nodes, tracks, graph, "Improved"))
    else:
        print("wrong method")

    end = time.time()
    print(len(formula.clauses), "Clauses were created in", end - start, "seconds.")

    """
     * ***** compute sat-solving-model if possible ***** *
    """

    solver = CustomSolver()
    solver.add(formula)

    start = time.time()
    model = solver.get_model() if solver.solve() else []
    end = time.time()

    if model:
        print("The Sat-Formula", model)
        print("calculated to", True, "in", end - start, "seconds.")
    else:
        print("No Solution found for", tracks, "Tracks in", end - start, "seconds.")

    """
     * ***** print TLP configuration as text ***** *
    """
    track_list = get_position(model, nodes, tracks)

    if track_list and method != 1:
        print("\n" "The TLP has the following configuration: \n")
        order_list = get_order(model[nodes * tracks:], nodes)

        for track_key in track_list:
            unordered_track_list = {key: order_list[key] for key in track_list[track_key] if key in order_list}
            ordered_track_list = dict(sorted(unordered_track_list.items(), key=lambda item: len(item[1]), reverse=True))
            track_list[track_key] = list(ordered_track_list.keys())

        track = ""
        for track_key in track_list:
            for sequence_node in track_list[track_key]:
                track += "  ----  " + str(sequence_node)
            print(track, " ---- ")
            track = ""
        return solver.solve()
    else:
        print("\n")
        return False

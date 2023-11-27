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
from Create_Formula import get_node_clauses, get_sequence_clauses_relation, get_sequence_total_order, get_sequence_clauses_relation_improved
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
        formula.extend(get_sequence_clauses_relation_improved(nodes, tracks, graph))
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
    track_list = get_position(model, nodes, tracks)
    # das kann weg
    # print(track_list)

    if track_list:
        print("\n" "The TLP has the following configuration: \n")
        order_list = get_order(model[nodes * tracks:], nodes, tracks, 1)

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


"""
    if method == 1 and model:
        order_list = get_order(model[nodes * tracks:], nodes, tracks, 1)

        for track_key in track_list:
            unordered_track_list = {key: order_list[key] for key in track_list[track_key] if key in order_list}
            ordered_track_list = dict(sorted(unordered_track_list.items(), key=lambda item: len(item[1]), reverse=True))
            track_list[track_key] = list(ordered_track_list.keys())

        track = ""
        for track_key in track_list:
            for sequence_node in track_list[track_key]:
                track += "  ----  " + str(sequence_node)
            print(track)
            track = ""

        # TO DO
    elif method == 2 and model:
        get_order(model[nodes * tracks:], nodes, tracks, 2)
    elif not model:
        print("No Solution found for", tracks, "tracks")
    else:
        print("wrong method")

    return solver.solve()
"""

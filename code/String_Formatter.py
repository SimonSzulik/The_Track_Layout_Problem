"""
 * ************************
 *	Bachelor-Thesis Simon Szulik
 *
 *      The Track Layout Problem
 *      from a SAT-Solving Perspective
 *
 * ************************
"""


def get_position(variables, nodes, tracks):
    track_list = {}
    for t in range(1, tracks + 1):
        track_list[t] = []
    if not variables:
        print("No Solution found")
        return
    for node in range(1, nodes + 1):
        for track in range(1, tracks + 1):
            if variables[((node - 1) * tracks + track) - 1] > 0:
                track_list[track].append(node)
    return track_list


def get_order(variables, nodes, tracks, order):
    order_list = {}
    if variables:
        match order:
            case 1:
                variables = sorted(variables, key=lambda x: abs(x))
                right_list = []
                for node in range(1, nodes + 1):
                    for node_2 in range(1, nodes + 1):
                        if variables[((node - 1) * nodes + node_2) - 1] > 0:
                            right_list.append(node_2)
                    if not right_list:
                        order_list[node] = []
                    else:
                        order_list[node] = right_list
                        right_list = []
            case 2:
                variables = sorted(variables, key=lambda x: abs(x))
                for node in range(1, nodes + 1):
                    for node_2 in range(1, nodes + 1):
                        if variables[((node - 1) * nodes + node_2) - 1] > 0:
                            print(f"Node {node} is on Position {node_2}")
    return order_list

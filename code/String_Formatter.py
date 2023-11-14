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
    if not variables:
        print("No Solution found")
        return
    for node in range(1, nodes + 1):
        for track in range(1, tracks + 1):
            if variables[((node - 1) * tracks + track) - 1] > 0:
                print(f"Node {node} is on track {track}")
    return


def get_order(variables, nodes, tracks, order):
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
                        print(f"Node {node} has no right neighbor")
                    else:
                        print(f"Node {node} lies left of Node {right_list}")
                        right_list = []
            case 2:
                variables = sorted(variables, key=lambda x: abs(x))
                for node in range(1, nodes + 1):
                    for node_2 in range(1, nodes + 1):
                        if variables[((node - 1) * nodes + node_2) - 1] > 0:
                            print(f"Node {node} is on Position {node_2}")
    return

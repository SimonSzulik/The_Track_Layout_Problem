"""
 * ************************
 *	Bachelor-Thesis Simon Szulik WS 2023/24
 *
 *      The Track Layout Problem
 *      from a SAT-Solving Perspective
 *
 * ************************
"""

"""
 * ***** help method to print out track-layout-configuration ***** *
"""


def get_position(variables, nodes, tracks):
    track_list = {}
    for t in range(1, tracks + 1):
        track_list[t] = []
    if not variables:
        return
    for node in range(1, nodes + 1):
        for track in range(1, tracks + 1):
            if variables[((node - 1) * tracks + track) - 1] > 0:
                track_list[track].append(node)
    return track_list


def get_order(variables, nodes):
    order_list = {}
    if variables:
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

    return order_list

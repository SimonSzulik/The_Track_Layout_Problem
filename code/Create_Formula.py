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
from itertools import combinations as combi
from pysat.formula import CNF

"""
 * ***** σ-Vars and it's clauses ***** *
 * ***** Which node is on which track? ***** *
 * ***** each node has t variables ***** *
"""

node_track_variable = [[]]
relational_sequence = [[]]
total_sequence = [[]]


def get_node_clauses(nodes, tracks, edges):
    global node_track_variable
    # nodes * tracks variables
    node_track_variable = [[0 for _ in range(tracks)] for _ in range(nodes)]
    unique_number = 1
    formula = CNF()
    neighbor_list = []

    # loop through variables and assign unique number
    for node in range(nodes):
        for track in range(tracks):
            node_track_variable[node][track] = unique_number
            unique_number += 1
        # append variable to formula
        formula.append([node_track_variable[node][track] for track in range(tracks)])

        # clause for the uniqueness of tracks per node
        for comb in combi([node_track_variable[node][track] for track in range(tracks)], 2):
            formula.append([-comb[0], -comb[1]])

    # search for all neighbored nodes
    for node1, node2 in enumerate(edges):
        neighbors = [j for j, node in enumerate(node2) if node == 1]
        for neighbor in neighbors:
            neighbor_list.append((node1, neighbor))

    # add restrictive neighbor clauses
    for neighbor in neighbor_list:
        for track in range(tracks):
            formula.append([-node_track_variable[neighbor[0]][track], -node_track_variable[neighbor[1]][track]])

    return formula


"""
 * ***** ω and and its clauses  ***** *
 * ***** first i variables stand for the node n to be left of node m on track t ***** *
"""


def get_sequence_clauses_relation(nodes, tracks, edges):  # Variable ω
    # wie viele variablen ?
    global relational_sequence
    relational_sequence = [[0 for _ in range(nodes)] for _ in range(nodes)]
    unique_number = nodes * tracks + 100
    formula = CNF()

    # loop through variables and assign unique number
    for left_node in range(nodes):
        for right_node in range(nodes):
            relational_sequence[left_node][right_node] = unique_number
            unique_number += 1
            # append clause to formula that negates i == j case
            if left_node == right_node:
                formula.append([-relational_sequence[left_node][right_node]])
        # append variable to formula
        # Das brauche ich nicht. da sonst bei jeder mind. 1 wahr wird !!
        # formula.append([relational_sequence[left_node][right_node] for right_node in range(nodes)])

    # asymmetric
    # wie viele klauseln ?
    for left_node in range(nodes):
        for right_node in range(nodes):
            if left_node < right_node:
                formula.append(
                    [-relational_sequence[left_node][right_node], -relational_sequence[right_node][left_node]])
                formula.append([relational_sequence[right_node][left_node], relational_sequence[left_node][right_node]])

    # transitivity
    # wie viee klauseln ?
    for left_node in range(nodes):
        for middle_node in range(nodes):
            for right_node in range(nodes):
                if left_node != middle_node and middle_node != right_node and left_node != right_node:
                    formula.append([-relational_sequence[left_node][middle_node],
                                    -relational_sequence[middle_node][right_node],
                                    relational_sequence[left_node][right_node]])

    # No crosses
    # first get all disjuct pairs
    # ersten t variablen in track_node_var gehören zu knoten 0, etc...
    edge_pairs = get_disjoint_edge_pairs(edges)
    track_pairs = get_track_pairs(tracks)
    print(edge_pairs)
    #  print(track_pairs)
    #  print(node_track_variable)
    #  print(relation_sequence)

    #  for t in range(2):
    #      print(t)

    # wie viele klauseln ?
    for edge_pair in edge_pairs:
        for track_pair in track_pairs:
            for swap in range(2):
                if swap == 0:
                    formula.append([-node_track_variable[edge_pair[0][0]][track_pair[0]],
                                    -node_track_variable[edge_pair[1][0]][track_pair[0]],
                                    -node_track_variable[edge_pair[0][1]][track_pair[1]],
                                    -node_track_variable[edge_pair[1][1]][track_pair[1]],
                                    -relational_sequence[edge_pair[0][0]][edge_pair[1][0]],
                                    -relational_sequence[edge_pair[1][1]][edge_pair[0][1]]])

                    formula.append([-node_track_variable[edge_pair[0][0]][track_pair[0]],
                                    -node_track_variable[edge_pair[1][0]][track_pair[0]],
                                    -node_track_variable[edge_pair[0][1]][track_pair[1]],
                                    -node_track_variable[edge_pair[1][1]][track_pair[1]],
                                    -relational_sequence[edge_pair[1][0]][edge_pair[0][0]],
                                    -relational_sequence[edge_pair[0][1]][edge_pair[1][1]]])
                else:
                    formula.append([-node_track_variable[edge_pair[0][1]][track_pair[0]],
                                    -node_track_variable[edge_pair[1][1]][track_pair[0]],
                                    -node_track_variable[edge_pair[0][0]][track_pair[1]],
                                    -node_track_variable[edge_pair[1][0]][track_pair[1]],
                                    -relational_sequence[edge_pair[0][0]][edge_pair[1][0]],
                                    -relational_sequence[edge_pair[1][1]][edge_pair[0][1]]])

                    formula.append([-node_track_variable[edge_pair[0][1]][track_pair[0]],
                                    -node_track_variable[edge_pair[1][1]][track_pair[0]],
                                    -node_track_variable[edge_pair[0][0]][track_pair[1]],
                                    -node_track_variable[edge_pair[1][0]][track_pair[1]],
                                    -relational_sequence[edge_pair[1][0]][edge_pair[0][0]],
                                    -relational_sequence[edge_pair[0][1]][edge_pair[1][1]]])

    return formula


"""
 * ***** ϕ and and its clauses  ***** *
 * ***** first i variables stand for the node n to be left of node m on track t ***** *
"""


def get_sequence_total_order(nodes, tracks, edges):  # Variable ϕ
    # wie viele variablen ?
    global total_sequence
    total_sequence = [[0 for _ in range(nodes)] for _ in range(nodes)]
    unique_number = nodes * tracks + 100
    formula = CNF()

    # loop through variables and assign unique number
    for node in range(nodes):
        for position in range(nodes):
            total_sequence[node][position] = unique_number
            unique_number += 1

        # append variable to formula
        formula.append([total_sequence[node][position] for position in range(nodes)])
        # clause for the uniqueness of tracks per node
        for comb in combi([total_sequence[node][position] for position in range(nodes)], 2):
            formula.append([-comb[0], -comb[1]])

    # überschneidungsverbot !!
    # so, dass nicht mehrere knoten auf der selben position sein dürfen !!
    for node in range(nodes):
        for position in range(nodes):
            for node_2 in range(nodes):
                if node_2 == node:
                    continue
                formula.append([-total_sequence[node][position], -total_sequence[node_2][position]])

    # No crosses
    edge_pairs = get_disjoint_edge_pairs(edges)
    track_pairs = get_track_pairs(tracks)
    print(edge_pairs)
    print(track_pairs)

    for edge_pair in edge_pairs:
        for track_pair in track_pairs:
            for a in range(nodes):
                for b in range(nodes):
                    for c in range(nodes):
                        for d in range(nodes):
                            # all different
                            if len({a, b, c, d}) == 4:
                                if (a < b and c < d) or (b < a and d < c):
                                    for swap in range(2):
                                        if swap == 0:
                                            formula.append([-node_track_variable[edge_pair[0][0]][track_pair[0]],
                                                            -node_track_variable[edge_pair[1][0]][track_pair[0]],
                                                            -node_track_variable[edge_pair[0][1]][track_pair[1]],
                                                            -node_track_variable[edge_pair[1][1]][track_pair[1]],
                                                            -total_sequence[edge_pair[0][0]][a],
                                                            -total_sequence[edge_pair[1][0]][b],
                                                            -total_sequence[edge_pair[0][1]][d],
                                                            -total_sequence[edge_pair[1][1]][c]])
                                        else:
                                            formula.append([-node_track_variable[edge_pair[0][1]][track_pair[0]],
                                                            -node_track_variable[edge_pair[1][1]][track_pair[0]],
                                                            -node_track_variable[edge_pair[0][0]][track_pair[1]],
                                                            -node_track_variable[edge_pair[1][0]][track_pair[1]],
                                                            -total_sequence[edge_pair[0][0]][a],
                                                            -total_sequence[edge_pair[1][0]][b],
                                                            -total_sequence[edge_pair[0][1]][d],
                                                            -total_sequence[edge_pair[1][1]][c]])

    return formula


def get_disjoint_edge_pairs(edges):
    edge_list = [(i, j) for i in range(len(edges)) for j in range(len(edges[i])) if edges[i][j] == 1]
    disjoint_pairs = []

    for i in range(len(edge_list)):
        for j in range(i + 1, len(edge_list)):
            edge_1 = edge_list[i]
            edge_2 = edge_list[j]
            if set(edge_1).isdisjoint(set(edge_2)):
                disjoint_pairs.append((edge_1, edge_2))

    return disjoint_pairs


# so, dass nur track paare die direkt aufeinanderfolgen betrachtet werden
def get_track_pairs(tracks):
    track_pairs = []
    for i in range(1, tracks):
        track_pairs.append((i - 1, i))
    return track_pairs

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

node_track_variable = [[]]  # σ(v_i,t_k)
relational_sequence = [[]]  # ω(v_i,v_j)
total_sequence = [[]]  # ϕ(v_i,p)
same_track = [[]]  # ψ(v_i,v_j)

""" 
 * ***** σ-Vars and it's clauses ***** *
 * ***** each node n has t variables ***** *
 * ***** first i variables stand for the node n_i to be on track t_k ***** *
"""


def get_node_clauses(nodes, tracks, edges):
    # variable σ
    global node_track_variable

    node_track_variable = [[0 for _ in range(tracks)] for _ in range(nodes)]
    unique_number = 1
    formula = CNF()
    neighbor_list = []

    # loop through σ variables and assign unique number
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
            if (([-node_track_variable[neighbor[0]][track],
                  -node_track_variable[neighbor[1]][track]] not in formula.clauses) and
                    ([-node_track_variable[neighbor[1]][track],
                      -node_track_variable[neighbor[0]][track]] not in formula.clauses)):
                formula.append([-node_track_variable[neighbor[0]][track], -node_track_variable[neighbor[1]][track]])

    return formula


""" approach 2 and its improved version
 * ***** ω and and its clauses with improvement variable ψ, that shows if n_i and n_j are on the same track ***** *
 * ***** first j variables stand for the node n_i to be left of node n_j ***** *
 * ***** ψ lets us ignore another for loop and reduce clauses for cross checking ***** *
"""


def get_sequence_clauses_relation(nodes, tracks, edges, version):
    # variables ω and ψ
    global relational_sequence
    global same_track

    relational_sequence = [[0 for _ in range(nodes)] for _ in range(nodes)]
    same_track = [[0 for _ in range(nodes)] for _ in range(nodes)]
    unique_number = nodes * tracks + 100
    unique_number_same_track = (nodes * tracks) + (nodes * nodes) + 100
    formula = CNF()

    # loop through ω variables and assign unique number
    for left_node in range(nodes):
        for right_node in range(nodes):
            relational_sequence[left_node][right_node] = unique_number
            unique_number += 1
            # append clause to formula that negates i == j case
            if left_node == right_node:
                formula.append([-relational_sequence[left_node][right_node]])

    # asymmetric
    for left_node in range(nodes):
        for right_node in range(nodes):
            if left_node < right_node:
                # when both are on same track
                for track in range(tracks):
                    formula.append([-node_track_variable[left_node][track], -node_track_variable[right_node][track],
                                    relational_sequence[left_node][right_node],
                                    relational_sequence[right_node][left_node]])
                formula.append(
                    [-relational_sequence[left_node][right_node], -relational_sequence[right_node][left_node]])

    # transitivity
    for left_node in range(nodes):
        for middle_node in range(nodes):
            for right_node in range(nodes):
                if left_node != middle_node and middle_node != right_node and left_node != right_node:
                    formula.append([-relational_sequence[left_node][middle_node],
                                    -relational_sequence[middle_node][right_node],
                                    relational_sequence[left_node][right_node]])

    # Implication to ensure sequenced nodes are on the same track
    for left_node in range(nodes):
        for right_node in range(nodes):
            for track in range(tracks):
                if left_node != right_node:
                    formula.append([-relational_sequence[left_node][right_node], node_track_variable[right_node][track],
                                    -node_track_variable[left_node][track]])

    # No Crossings
    edge_pairs = get_disjoint_edge_pairs(edges)
    track_pairs = get_track_pairs(tracks)

    if version == "Improved":
        # loop through ψ variables and assign unique number
        for node_1 in range(nodes):
            for node_2 in range(nodes):
                same_track[node_1][node_2] = unique_number_same_track
                unique_number_same_track += 1

        for node_1 in range(nodes):
            for node_2 in range(nodes):
                if node_1 < node_2:
                    for track in range(tracks):
                        formula.append([-node_track_variable[node_1][track], -node_track_variable[node_2][track],
                                        same_track[node_1][node_2]])
                       # formula.append([same_track[node_1][node_2], -same_track[node_2][node_1]])
                        #formula.append([-same_track[node_1][node_2], same_track[node_2][node_1]])

        for edge_pair in edge_pairs:
            formula.append([-same_track[min(edge_pair[0][0], edge_pair[1][0])][max(edge_pair[0][0], edge_pair[1][0])],
                           -same_track[min(edge_pair[0][1], edge_pair[1][1])][max(edge_pair[0][1], edge_pair[1][1])],
                          #  -same_track[edge_pair[0][1]][edge_pair[1][1]],
                            -relational_sequence[edge_pair[0][0]][edge_pair[1][0]],
                            -relational_sequence[edge_pair[1][1]][edge_pair[0][1]]])

            formula.append([-same_track[min(edge_pair[0][0], edge_pair[1][0])][max(edge_pair[0][0], edge_pair[1][0])],
                            -same_track[min(edge_pair[0][1], edge_pair[1][1])][max(edge_pair[0][1], edge_pair[1][1])],
                            -relational_sequence[edge_pair[1][0]][edge_pair[0][0]],
                            -relational_sequence[edge_pair[0][1]][edge_pair[1][1]]])
    else:
        for edge_pair in edge_pairs:
            for track_pair in track_pairs:
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
    return formula


""" approach 1 (bad and slow since its creating a HUGE amount of clauses to check crossings)
 * ***** ϕ and and its clauses  ***** *
 * ***** first i variables stand for the node n being on position p_i ***** *
 * ***** This approach will not be further elaborated since it seems to be a way worse option ***** *
"""


def get_sequence_total_order(nodes, tracks, edges):
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

    # No Overlaps -> no 2 Nodes have the same Position
    for node in range(nodes):
        for position in range(nodes):
            for node_2 in range(nodes):
                if node_2 == node:
                    continue
                formula.append([-total_sequence[node][position], -total_sequence[node_2][position]])

    # No Crossings
    edge_pairs = get_disjoint_edge_pairs(edges)
    track_pairs = get_track_pairs(tracks)

    for edge_pair in edge_pairs:
        for track_pair in track_pairs:
            for a in range(nodes):
                for b in range(nodes):
                    for c in range(nodes):
                        for d in range(nodes):
                            # all different
                            if len({a, b, c, d}) == 4:
                                if a < b and c < d:
                                    formula.append([-node_track_variable[edge_pair[0][0]][track_pair[0]],
                                                    -node_track_variable[edge_pair[1][0]][track_pair[0]],
                                                    -node_track_variable[edge_pair[0][1]][track_pair[1]],
                                                    -node_track_variable[edge_pair[1][1]][track_pair[1]],
                                                    -total_sequence[edge_pair[0][0]][a],
                                                    -total_sequence[edge_pair[1][0]][b],
                                                    -total_sequence[edge_pair[0][1]][d],
                                                    -total_sequence[edge_pair[1][1]][c]])
    return formula


# help function to all edge pairs to check for crossings
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


# help function to get track pairs
def get_track_pairs(tracks):
    track_numbers = list(range(0, tracks))
    track_pairs = []
    track_pairs.extend(combi(track_numbers, 2))

    return track_pairs

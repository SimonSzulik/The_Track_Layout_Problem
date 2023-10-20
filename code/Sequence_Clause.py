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
 * ***** create variables for node sequences on the tracks // yijk ***** *
 * ***** first i variables stand for the node n to be left of node m on track t ***** *
"""


def get_sequence_clauses_relation(nodes, tracks, edges):
    # nodes * nodes * tracks variables
    variables = [[[0 for _ in range(nodes)] for _ in range(nodes)] for _ in range(tracks)]
    unique_number = nodes * tracks + 100
    formula = CNF()

    for left_node in range(nodes):
        for right_node in range(nodes):
            for track in range(tracks):
                variables[left_node][right_node][track] = unique_number
                unique_number += 1
                # append clause to formula that negates i == j case
                if left_node == right_node:
                    formula.append([-variables[left_node][right_node][track]])
            # append variables to formula
            # formula.append([variables[left_node][right_node][track] for track in range(tracks)])
            # --> dont need this one

            # clause for the uniqueness of relation and asymmetric
            # care for case that a node has no right neighbor
            for comb in combi([variables[left_node][right_node][track] for track in range(tracks)], 2):
                formula.append([-comb[0], -comb[1]])

    return formula


"""
 * ***** create variables for node sequences on the tracks // yijp ***** *
 * ***** first i variables stand for the node n to be at place j on track p ***** *
"""


def get_sequence_clauses_per_track(nodes, tracks, edges):
    # nodes * nodes * tracks variables
    variables = [[[0 for _ in range(nodes)] for _ in range(nodes)] for _ in range(tracks)]
    unique_number = nodes * tracks + 100
    formula = CNF()

    for node in range(nodes):
        for place in range(nodes):
            for track in range(tracks):
                variables[node][place][track] = unique_number
                unique_number += 1

            # append variables to formula
            formula.append([variables[node][place][track] for track in range(tracks)])

            # clause for the uniqueness of sequence per track
            for comb in combi([variables[node][place][track] for track in range(tracks)], 2):
                formula.append([-comb[0], -comb[1]])

    return formula

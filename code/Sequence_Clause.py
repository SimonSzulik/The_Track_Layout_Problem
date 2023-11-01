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
 * ***** ω,ϕ and and its clauses  ***** *
 * ***** first i variables stand for the node n to be left of node m on track t ***** *
"""


def get_sequence_clauses_relation(nodes, tracks):
    # nodes * nodes * - nodes
    variables = [[0 for _ in range(tracks)] for _ in range(nodes)]
    unique_number = nodes * tracks + 100
    formula = CNF()

    for left_node in range(nodes):
        for right_node in range(nodes):
            variables[left_node][right_node] = unique_number
            unique_number += 1
            # append clause to formula that negates i == j case
            if left_node == right_node:
                formula.append([-variables[left_node][right_node]])
        #     print(formula.clauses)
        # asymmetric
        #  else:
        #     print(left_node, right_node)
        #    formula.append([-variables[left_node][right_node], -variables[right_node][left_node]])
        #   formula.append([variables[right_node][left_node], variables[left_node][right_node]])
        # possible variables
        formula.append([variables[left_node][right_node] for right_node in range(nodes)])

    # asymmetric
    for left_node in range(nodes):
        for right_node in range(nodes):
            if left_node != right_node:
                formula.append([-variables[left_node][right_node], -variables[right_node][left_node]])
                formula.append([variables[right_node][left_node], variables[left_node][right_node]])
    # transitivity
    for left_node in range(nodes):
        for middle_node in range(nodes):
            for right_node in range(nodes):
                if left_node != middle_node and middle_node != right_node and left_node != right_node:
                    formula.append([-variables[left_node][middle_node], -variables[middle_node][right_node],
                                    variables[left_node][right_node]])

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

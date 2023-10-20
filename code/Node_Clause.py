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
 * ***** create variables for node assignment to track // xij ***** *
 * ***** create clauses to restrict a node to have a unique track ***** *
 * ***** create clauses to restrict neighbor nodes having the same track ***** *
 * ***** first i variables stand for the i-th node to be on track t in range of tracks ***** *
"""


def get_node_clauses(nodes, tracks, edges):
    # nodes * tracks variables
    variables = [[0 for _ in range(tracks)] for _ in range(nodes)]
    unique_number = 1
    formula = CNF()
    neighbor_list = []

    # loop through variables and assign unique number
    for node in range(nodes):
        for track in range(tracks):
            variables[node][track] = unique_number
            unique_number += 1
        # append variable to formula
        formula.append([variables[node][track] for track in range(tracks)])

        # clause for the uniqueness of tracks per node
        for comb in combi([variables[node][track] for track in range(tracks)], 2):
            formula.append([-comb[0], -comb[1]])

    # search for all neighbored nodes
    for node1, node2 in enumerate(edges):
        neighbors = [j for j, node in enumerate(node2) if node == 1]
        for neighbor in neighbors:
            neighbor_list.append((node1, neighbor))

    # add restrictive neighbor clauses
    for neighbor in neighbor_list:
        for track in range(tracks):
            formula.append([-variables[neighbor[0]][track], -variables[neighbor[1]][track]])

    return formula

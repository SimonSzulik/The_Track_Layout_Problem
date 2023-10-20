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
from itertools import combinations
from pysat.formula import CNF
from pysat.solvers import Lingeling

"""
 * ***** Beispielgraph ***** *
"""
n = 4
pages = 4

edges = [[0 for _ in range(n)] for _ in range(n)]

# complete graph
for i in range(n - 1):
    for j in range(i + 1, n):
        edges[i][j] = 1
"""
 * ***** Beispielgraph ***** *
"""

"""
 * ***** variables for node assignment to track // xij ***** *
"""
variables = [[0 for _ in range(pages)] for _ in range(n)]
# print(variables)

varNumber = 1
formula = CNF()

# loop through variables and assign unique number
for i in range(n):
    for j in range(pages):
        variables[i][j] = varNumber
        varNumber += 1
    # append variable to formula
    formula.append([variables[i][j] for j in range(pages)])

    # clause for the uniqueness of tracks per node
    for comb in combinations([variables[i][j] for j in range(pages)], 2):
        formula.append([-comb[0], -comb[1]])
"""
 * ***** variables for node assignment to track // xij ***** *
"""

# print(formula.clauses)
# print(variables)

"""
 * ***** restrict neighbor nodes on same track// xij ***** *
"""
nachbarn_tupel = []

# search for all neighbor nodes
for i, zeile in enumerate(edges):
    nachbarn = [j for j, wert in enumerate(zeile) if wert == 1]
    for nachbar in nachbarn:
        nachbarn_tupel.append((i, nachbar))

# print(nachbarn_tupel)

for nachbarn in nachbarn_tupel:
    for t in range(pages):
        #print(-variables[nachbarn[0]][t], -variables[nachbarn[1]][t])
        formula.append([-variables[nachbarn[0]][t], -variables[nachbarn[1]][t]])
"""
 * ***** restrict neighbor nodes on same track// xij ***** *
"""

"""
 * ***** Sat Solving ***** *
"""
with Lingeling(bootstrap_with=formula.clauses, with_proof=False) as ling:
    print(ling.solve())
    print(ling.get_model())
"""
 * ***** Sat Solving ***** *
"""


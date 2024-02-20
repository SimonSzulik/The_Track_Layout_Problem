"""
 * ************************
 *	Bachelor-Thesis Simon Szulik WS 2023/24
 *
 *      The Track Layout Problem
 *      from a SAT-Solving Perspective
 *
 * ************************
"""

from pysat.solvers import Lingeling

"""
 * ***** custom solver to prevent adding non used variables in Lingelin ***** *
 * *****                     mainly for readability                     ***** *
"""


class CustomSolver:
    def __init__(self):
        self.solver = Lingeling()
        self.var_map = {}
        self.reverse_map = {}
        self.next_internal_var = 1
        self.clauses = []

    def add_clause(self, clause):
        internal_clause = []
        for var in clause:
            if abs(var) not in self.var_map:
                self.var_map[abs(var)] = self.next_internal_var
                self.reverse_map[self.next_internal_var] = abs(var)
                self.next_internal_var += 1
            internal_var = self.var_map[abs(var)]
            if var < 0:
                internal_var = -internal_var
            internal_clause.append(internal_var)
        self.solver.add_clause(internal_clause)
        self.clauses.append(clause)

    def add(self, formula):
        for clause in formula:
            self.add_clause(clause)

    def solve(self):
        return self.solver.solve()

    def get_model(self):
        internal_model = self.solver.get_model()
        return [self.reverse_map[abs(var)] * (1 if var > 0 else -1) for var in internal_model]


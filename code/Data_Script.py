"""
 * ************************
 *	Bachelor-Thesis Simon Szulik
 *
 *      The Track Layout Problem
 *      from a SAT-Solving Perspective
 *
 * ************************
"""

import os
import networkx as nx


def get_dataset():
    data_set = []
    with open('../Data_Sets/Data_Set_10*n_Nodes.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            data_set.append(line.strip())

        # Path to dataset
        data_folder_path = '../data'
        test_graphs = {}

        # Loop through dataset
        for filename in os.listdir(data_folder_path):
            if filename in data_set:
                file_path = os.path.join(data_folder_path, filename)
                graph = nx.read_gml(file_path)
                test_graphs[filename] = nx.to_numpy_array(graph)

    return test_graphs

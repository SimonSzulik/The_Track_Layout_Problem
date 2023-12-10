"""
 * ************************
 *	Bachelor-Thesis Simon Szulik WS 2023/24
 *
 *      The Track Layout Problem
 *      from a SAT-Solving Perspective
 *
 * ************************
"""

import os
import networkx as nx

"""
 * ***** function to load smaller dataset from rome_gml ***** *
"""


def get_dataset(data):
    data_set = []
    with open(data, 'r') as f:
        lines = f.readlines()
        for line in lines:
            data_set.append(line.strip())

        # path to dataset
        data_folder_path = '../data'
        test_graphs = {}

        # loop through dataset and return the wanted graph data
        for filename in os.listdir(data_folder_path):
            if filename in data_set:
                file_path = os.path.join(data_folder_path, filename)
                graph = nx.read_gml(file_path)
                test_graphs[filename] = nx.to_numpy_array(graph)

    return test_graphs

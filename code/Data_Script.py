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
    # Path to dataset
    data_folder_path = '../data'

    test_graphs = {}
    counter = 0
    # Loop through dataset
    for filename in os.listdir(data_folder_path):
        if filename.endswith('.gml'):
            file_path = os.path.join(data_folder_path, filename)

            graph = nx.read_gml(file_path)

            num_nodes = graph.number_of_nodes()
            num_edges = graph.number_of_edges()

            # graph dependencies
            if num_nodes == 10:
                # print(f"File: {filename}, Nodes: {num_nodes}, Edges: {num_edges}")
                # print("------")
                test_graphs[filename] = nx.to_numpy_array(graph)
                counter += 1
            if counter == 1:
                break

    return test_graphs

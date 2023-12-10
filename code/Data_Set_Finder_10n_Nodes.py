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
 * ***** loop through dataset and find 200 graphs ***** *
 * 20 with 10 nodes
 * 20 with 20 nodes
 * 20 with 30 nodes
 * ...
 * ...
 * ...
 * 20 with 100 nodes
"""

# Path to dataset
data_folder_path = '../data'

with open('../Data_Sets/Data_Set_10n_Nodes.txt', 'w') as f:
    for factor in range(1, 11):
        counter = 0
        for filename in os.listdir(data_folder_path):
            if filename.endswith('.gml'):
                file_path = os.path.join(data_folder_path, filename)

                graph = nx.read_gml(file_path)

                num_nodes = graph.number_of_nodes()
                num_edges = graph.number_of_edges()

                # graph dependencies and writing
                if num_nodes == 10 * factor:
                    print(f"File: {filename}, Nodes: {num_nodes}, Edges: {num_edges}")
                    print("------")
                    f.write(filename)
                    f.write("\n")
                    counter += 1
                if counter == 20:
                    break

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

# Path to dataset
data_folder_path = '../data'

"""
 * ***** Loop through Dataset and find 100 graphs ***** *
 * 10 with 10 nodes
 * 10 with 20 nodes
 * 10 with 30 nodes
 * ...
 * ...
"""
with open('../Data_Sets/Data_Set_10*n_Nodes.txt', 'w') as f:
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
                if counter == 10:
                    break

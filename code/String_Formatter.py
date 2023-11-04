def get_position(variables, nodes, tracks):
    for node in range(1, nodes + 1):
        for track in range(1, tracks + 1):
            if variables[((node - 1) * nodes + track)-1] > 0:
                print(f"Node {node} is on track {track}")


def get_sequence(variables, nodes, tracks):
    variables = sorted(variables, key=lambda x: abs(x))
    right_list = []

    for node in range(1, nodes + 1):
        for node_2 in range(1, tracks + 1):
            if variables[((node - 1) * nodes + node_2)-1] > 0:
                right_list.append(node_2)
        if not right_list:
            print(f"Node {node} has no right neighbor")
        else:
            print(f"Node {node} lies left of Node {right_list}")
            right_list = []

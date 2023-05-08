# Adjacency Matrix representation in Python


class Graph(object):

    # Initialize the matrix
    def __init__(self, size):
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
        self.size = size
        self.node_dict = {}

    # Add a node
    def add_node(self, node_label):
        if node_label in self.node_dict:
            print("Node %s already exists." % node_label)
            return
        node_num = len(self.node_dict)
        self.node_dict[node_label] = node_num
        self.adjMatrix.append([0] * (self.size + 1))
        self.size += 1
        for row in self.adjMatrix:
            row.append(0)

    # Add edges
    def add_edge(self, v1, v2):
        if v1 not in self.node_dict:
            self.add_node(v1)
        if v2 not in self.node_dict:
            self.add_node(v2)
        v1_num = self.node_dict[v1]
        v2_num = self.node_dict[v2]
        if v1_num == v2_num:
            print("Same vertex %s and %s" % (v1, v2))
        self.adjMatrix[v1_num][v2_num] = 1
        self.adjMatrix[v2_num][v1_num] = 1

    # Remove edges
    def remove_edge(self, v1, v2):
        if v1 not in self.node_dict or v2 not in self.node_dict:
            print("One or both nodes not found.")
            return
        v1_num = self.node_dict[v1]
        v2_num = self.node_dict[v2]
        if self.adjMatrix[v1_num][v2_num] == 0:
            print("No edge between %s and %s" % (v1, v2))
            return
        self.adjMatrix[v1_num][v2_num] = 0
        self.adjMatrix[v2_num][v1_num] = 0

    def __len__(self):
        return self.size

    # Print the matrix
    def print_matrix(self):
        for node_label in self.node_dict:
            print('\t%s' % node_label, end='')
        print()
        for i, row in enumerate(self.adjMatrix):
            print(self.node_dict_inv[i], end='')
            for val in row:
                print('\t{:4}'.format(val), end='')
            print()

    @property
    def node_dict_inv(self):
        return {v: k for k, v in self.node_dict.items()}


def main():
    g = Graph(8)
    g.add_edge("a", "b")
    g.add_edge("b", "c")
    g.add_edge("a", "d")
    g.add_edge("a", "e")
    g.add_edge("c", "e")
    g.add_edge("d", "e")
    g.add_edge("c", "f")
    g.add_edge("e", "f")
    g.print_matrix()


if __name__ == '__main__':
    main()
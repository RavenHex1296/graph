import sys
sys.path.append('src')
from graph import *


class Node():
    def __init__(self, index, value=None):
        self.index = index
        self.value = value
        self.neighbors = []
        self.previous = None
        self.d_value = 9999999999


class WeightedGraph():
    def __init__(self, weights, values):
        self.weights = weights
        self.values = values
        self.edges = [key for key in self.weights]
        indices = []

        for edge in self.edges:
            indices.append(edge[0])
            indices.append(edge[1])

        self.nodes = [Node(n, self.values[n]) for n in range(max(indices) + 1)]

    def build_from_edges(self):
        for edge in self.edges:
            self.nodes[edge[0]].neighbors.append(self.nodes[edge[1]])
            self.nodes[edge[1]].neighbors.append(self.nodes[edge[0]])

    def edge_weight(self, starting_node_index, next_node_index):
        for edge in self.weights:
            if starting_node_index.index in edge and next_node_index.index in edge:
                return self.weights[edge]

    def setup(self, starting_node_index):
        nodes = [node for node in self.nodes]
        self.nodes[starting_node_index].d_value = 0
        queue = [self.nodes[starting_node_index]]
        visited = []
        current_node = queue[0]

        while len(visited) < len(self.nodes):
            visited.append(current_node)
            nodes.remove(current_node)
            queue.remove(current_node)

            for neighbor in current_node.neighbors:
                if neighbor not in visited:
                    weight = self.edge_weight(current_node, neighbor)

                    if current_node.d_value + weight < neighbor.d_value:
                        neighbor.d_value = current_node.d_value + weight

                    neighbor.previous = current_node
                    queue.append(neighbor)

            if len(nodes) != 0:
                lesser_d_value = nodes[0].d_value
                current_node = nodes[0]

                for node in nodes:
                    if node.d_value < lesser_d_value:
                        current_node = node
                        lesser_d_value = node.d_value

    def calc_distance(self, starting_node_index, ending_node_index):
        self.setup(starting_node_index)

        if self.nodes[ending_node_index].d_value == None:
            return False

        return self.nodes[ending_node_index].d_value

    def calc_shortest_path(self, start_node, end_node):
        self.setup(start_node)
        shortest_path_tree_edges = []

        for (a, b) in self.edges:
            if self.nodes[b].d_value - self.nodes[a].d_value == self.weights[(a, b)]:
                shortest_path_tree_edges.append((a, b))

        shortest_path_tree = Graph(shortest_path_tree_edges)
        shortest_path_tree.build_from_edges()
        return shortest_path_tree.calc_shortest_path(start_node, end_node)

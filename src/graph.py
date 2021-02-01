class Node:
    def __init__(self, index, value=None):
        self.index = index
        self.neighbors = []
        self.value = value


class Graph:
    def __init__(self, edges):
        self.edges = edges
        indices = []

        for edge in edges:
            indices.append(edge[0])
            indices.append(edge[1])

        self.node = [Node(n) for n in range(max(indices) + 1)]

    def build_from_edges(self):
        for edge in self.edges:
            self.node[edge[0]].neighbors.append(self.node[edge[1]])
            self.node[edge[1]].neighbors.append(self.node[edge[0]])

    def get_nodes_breadth_first(self, root_index):
        queue = [self.node[root_index]]
        visited = []

        while len(queue) > 0:
            visited.append(queue[0])

            for neighbor in queue[0].neighbors:
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)

            queue.remove(queue[0])

        return visited

    def get_nodes_depth_first(self, root_index):
        stack = [self.node[root_index]]
        visited = []

        while len(stack) > 0:
            visited.append(stack[0])

            for neighbor in stack[0].neighbors:
                if neighbor not in visited and neighbor not in stack:
                    stack.insert(1, neighbor)

            stack.remove(stack[0])

        return visited

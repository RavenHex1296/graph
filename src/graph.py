class Node:
    def __init__(self, index, value=None):
        self.index = index
        self.neighbors = []
        self.value = value
        self.distance = 0
        self.previous = None


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

    def set_breadth_first_distance_and_previous(self, starting_node_index):
        self.node[starting_node_index].distance = 0
        queue = [self.node[starting_node_index]]
        visited = []

        while len(queue) > 0:
            current_node = queue[0]
            visited.append(current_node)
            queue.remove(current_node)

            for neighbor in current_node.neighbors:
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)
                    neighbor.distance = current_node.distance + 1
                    neighbor.previous = current_node

    def calc_distance(self, starting_node_index, ending_node_index):
        self.set_breadth_first_distance_and_previous(starting_node_index)
        return self.node[ending_node_index].distance
    
    def calc_shortest_path(self, starting_node_index,ending_node_index):
        self.set_breadth_first_distance_and_previous(starting_node_index)
        current_node = self.node[ending_node_index]
        reversed_path = [current_node]

        while current_node.index != starting_node_index:
            reversed_path.append(current_node.previous)
            current_node = current_node.previous

        return [node.index for node in reversed_path][::-1]

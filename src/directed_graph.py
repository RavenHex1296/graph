class Node:
    def __init__(self, index, value=None):
        self.index = index
        self.children = []
        self.parents = []
        self.value = value
        self.distance = 0
        self.previous = None

class DirectedGraph:
    def __init__(self, edges):
        self.edges = edges
        indices = []

        for edge in edges:
            indices.append(edge[0])
            indices.append(edge[1])

        self.nodes = [Node(n) for n in range(max(indices) + 1)]

    def build_from_edges(self):
        for edge in self.edges:
            self.nodes[edge[0]].children.append(self.nodes[edge[1]])
            self.nodes[edge[1]].parents.append(self.nodes[edge[0]])

    def nodes_breadth_first(self, root_index):
        queue = [self.nodes[root_index]]
        visited = []

        while len(queue) > 0:
            visited.append(queue[0])

            for child in queue[0].children:
                if child not in visited and child not in queue:
                    queue.append(child)

            queue.remove(queue[0])

        return visited

    def nodes_depth_first(self, root_index):
        stack = [self.nodes[root_index]]
        visited = []

        while len(stack) > 0:
            visited.append(stack[0])

            for child in stack[0].children:
                if child not in visited and child not in stack:
                    stack.insert(1, child)

            stack.remove(stack[0])

        return visited

    def set_breadth_first_distance_and_previous(self, starting_node_index):
        for node in self.nodes:
            node.distance = None
            node.previous = None

        self.nodes[starting_node_index].distance = 0
        queue = [self.nodes[starting_node_index]]
        visited = []

        while len(queue) > 0:
            current_node = queue[0]
            visited.append(current_node)
            queue.remove(current_node)

            for child in current_node.children:
                if child not in visited and child not in queue:
                    queue.append(child)
                    child.distance = current_node.distance + 1
                    child.previous = current_node

    def calc_distance(self, starting_node_index, ending_node_index):
        self.set_breadth_first_distance_and_previous(starting_node_index)

        if self.nodes[ending_node_index].distance == None:
            return False

        return self.nodes[ending_node_index].distance
    
    def calc_shortest_path(self, starting_node_index, ending_node_index):
        self.set_breadth_first_distance_and_previous(starting_node_index)
        current_node = self.nodes[ending_node_index]
        reversed_path = [current_node.index]

        if current_node.distance == None:
            return False

        while current_node.index != starting_node_index:
            reversed_path.append(current_node.previous.index)
            current_node = current_node.previous

        return reversed_path[::-1]

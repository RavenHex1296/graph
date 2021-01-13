class Node:
    def __init__(self, parent, value, children):
        self.parent = parent
        self.value = value
        self.children = children


class Tree:
    def __init__(self, edges):
        self.edges = edges
        self.root = Node(None, self.get_root(self.edges), None)

    def get_children(self, node, tree):
        children = []

        for edge in tree:
            if edge[0] == node:
                children.append(edge[1])

        return children

    def get_parents(self, node, tree):
        for edge in tree:
            if edge[1] == node:
                return edge[0]

    def get_root(self, tree):
        for edge in tree:
            if self.get_parents(edge[0], tree) == None:
                return edge[0]

    def build_from_edges(self):
        current_nodes = [self.root]

        while len(current_nodes) != 0:
            latest_children = []

            for node in current_nodes:
                children = self.get_children(node.value, self.edges)

                for n in range(len(children)):
                    children[n] = Node(node, children[n], None)

                node.children = children

                for n in children:
                    latest_children.append(n)

            current_nodes = list(latest_children)

    def nodes_breadth_first(self):
        queue = [self.root]
        visited = []

        while len(queue) > 0:
            visited.append(queue[0])

            if queue[0].children != None:
                for node_child in queue[0].children:
                    queue.append(node_child)

            queue.remove(queue[0])

        return visited

    def nodes_depth_first(self):
        stack = [self.root]
        visited = []

        while len(stack) > 0:
            visited.append(stack[0])

            if stack[0].children != None:
                for child in stack[0].children:
                    stack.insert(1, child)

            stack.remove(stack[0])

        return visited

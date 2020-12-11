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

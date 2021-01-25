import sys
sys.path.append('src')
from tree import Tree
'''
edges = [('a', 'c'), ('e', 'g'), ('e', 'i'), ('e', 'a'), ('g', 'b'), ('a', 'd'), ('d', 'f'), ('f', 'h'), ('d', 'j'), ('c', 'k')]
tree = Tree(edges)
tree.build_from_edges()

print("Asserting root value")
assert tree.root.value == 'e', "Incorrect output"
print("PASSED")

print("Asserting the children of e")
assert [node.value for node in tree.root.children] == ['g', 'i', 'a'], "Incorrect output"
print("PASSED")

print("Asserting the children of a")
assert [node.value for node in tree.root.children[2].children] == ['c', 'd'], "Incorrect output"
print("PASSED")

print("Asserting the children of i")
assert [node.value for node in tree.root.children[1].children] == [], "Incorrect output"
print("PASSED")

print("Asserting the children of g")
assert [node.value for node in tree.root.children[0].children] == ['b'], "Incorrect output"
print("PASSED")

print("Asserting the children of c")
assert [node.value for node in tree.root.children[2].children[0].children] == ['k'], "Incorrect output"
print("PASSED")

print("Asserting the children of d")
assert [node.value for node in tree.root.children[2].children[1].children] == ['f', 'j'], "Incorrect output"
print("PASSED")

print("Asserting the children of b")
assert [node.value for node in tree.root.children[0].children[0].children] == [], "Incorrect output"
print("PASSED")

print("Asserting the children of k")
assert [node.value for node in tree.root.children[2].children[0].children[0].children] == [], "Incorrect output"
print("PASSED")

print("Asserting the children of j")
assert [node.value for node in tree.root.children[2].children[1].children[1].children] == [], "Incorrect output"
print("PASSED")

print("Asserting the children of f")
assert [node.value for node in tree.root.children[2].children[1].children[0].children] == ['h'], "Incorrect output"
print("PASSED")

print("Asserting the children of h")
assert [node.value for node in tree.root.children[2].children[1].children[0].children[0].children] == [], "Incorrect output"
print("PASSED")

edges = [('a', 'c'), ('e', 'g'), ('e', 'i'), ('e', 'a'), ('d', 'b'), ('a', 'd'), ('d', 'f'), ('f', 'h'), ('d', 'j'), ('d', 'k')]
tree = Tree(edges)
tree.build_from_edges()

print("Asserting nodes_breadth_first")
nodes = tree.nodes_breadth_first()
assert [node.value for node in nodes] == ['e', 'g', 'i', 'a', 'c', 'd', 'b', 'f', 'j', 'k', 'h'], "Incorrect answer"
print("PASSED")

print("Asserting nodes_depth_first")
nodes = tree.nodes_depth_first()
assert [node.value for node in nodes] == ['e', 'a', 'd', 'k', 'j', 'f', 'h', 'b', 'c', 'i', 'g'], "Incorrect answer"
print("PASSED")
'''

node_values = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
edges = [(0, 2), (4, 6), (4, 8), (4, 0), (3, 1), (0, 3), (3, 5), (5, 7), (3, 9), (3, 10)]

tree = Tree(edges, node_values)
tree.build_from_edges()

assert tree.root.value == 'e'
assert tree.root.index == 4
children = set(tree.root.children)

grandchildren = set([])
for child in children:
    grandchildren = grandchildren.union(set(child.children))

great_grandchildren = set([])
for grandchild in grandchildren:
    great_grandchildren = great_grandchildren.union(set(grandchild.children))

great_great_grandchildren = set([])
for great_grandchild in great_grandchildren:
    great_great_grandchildren = great_great_grandchildren.union(set(great_grandchild.children))

assert {node.index for node in children} == {0, 8, 6}
assert {node.value for node in children} == {'a', 'i', 'g'}

assert {node.index for node in grandchildren} == {2, 3}
assert {node.value for node in grandchildren} == {'c', 'd'}

assert {node.index for node in great_grandchildren} == {1, 9, 5, 10}
assert {node.value for node in great_grandchildren} == {'b', 'j', 'f', 'k'}

assert {node.index for node in great_great_grandchildren} == {7}
assert {node.value for node in great_great_grandchildren} == {'h'}


node_values = ['a', 'b', 'a', 'a', 'a', 'b', 'a', 'b', 'a', 'b', 'b']
tree = Tree(edges, node_values)
tree.build_from_edges()
assert tree.root.value == 'a' and tree.root.index == 4
children = set(tree.root.children)

grandchildren = set([])
for child in children:
    grandchildren = grandchildren.union(set(child.children))

great_grandchildren = set([])
for grandchild in grandchildren:
    great_grandchildren = great_grandchildren.union(set(grandchild.children))

great_great_grandchildren = set([])
for great_grandchild in great_grandchildren:
    great_great_grandchildren = great_great_grandchildren.union(set(great_grandchild.children))

assert {node.index for node in children} == {0, 8, 6}
assert {node.value for node in children} == {'a','a','a'}

assert {node.index for node in grandchildren} == {2,3}
assert {node.value for node in grandchildren} == {'a','a'}

assert {node.index for node in great_grandchildren} == {1,9,5,10}
assert {node.value for node in great_grandchildren} == {'b','b','b','b'}

assert {node.index for node in great_great_grandchildren} == {7}
assert {node.value for node in great_great_grandchildren} == {'b'}
print("EVERYTHING PASSED")
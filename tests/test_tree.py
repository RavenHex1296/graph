import sys
sys.path.append('src')
from tree import Tree

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

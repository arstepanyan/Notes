"""
Given two nodes in a binary tree, design an algorithm that computes their LCA.
Assume that each node has a parent pointer.

          3
       /     \
      5       1
    /  \     / \
   6    2   0   8
       / \
      7  4

LCA(5, 1) = 3
LCA(5, 4) = 5
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def find_lca(tree, node1, node2):
    return _find_lca(tree, node1, node2)


def _find_lca(tree, node1, node2):
    if not tree:
        return False

    if tree is node1:
        return node1.value
    if tree is node2:
        return node2.value

    left = _find_lca(tree.left, node1, node2)
    right = _find_lca(tree.right, node1, node2)

    if left and right:
        return tree.value

    return left or right


if __name__ == "__main__":
    tree = Node(3)
    tree.left = Node(5)
    tree.left.left = Node(6)
    tree.left.right = Node(2)
    tree.left.right.left = Node(7)
    tree.left.right.right = Node(4)

    tree.right = Node(1)
    tree.right.left = Node(0)
    tree.right.right = Node(8)

    print(find_lca(tree, tree.left, tree.right))
    print(find_lca(tree, tree.left, tree.left.right.right))

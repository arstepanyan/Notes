"""
Write a program that takes as input the root of a binary tree and checks whether the tree is height balanced.
A binary tree is said to be height-balanced if for each node in the tree,
the difference in the height of its left and right subtrees is at most one.
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, value):
        self.root = Node(value)

    def preorder_trav(self, start, traversal):
        """root -> left -> right"""
        if start:
            traversal += str(start.value) + '-'
            traversal = self.preorder_trav(start.left, traversal)
            traversal = self.preorder_trav(start.right, traversal)
        return traversal


def height_balanced(tree):
    if tree is None:
        return True
    return _height_balanced(tree) != -1


def _height_balanced(tree):
    if not tree:
        return 1
    left_h = _height_balanced(tree.left)
    right_h = _height_balanced(tree.right)

    if left_h == -1 or right_h == -1 or abs(left_h - right_h) > 1:
        return -1
    return 1 + max(left_h, right_h)


if __name__ == "__main__":
    tree = BinaryTree('A')
    tree.root.left = Node('B')
    tree.root.left.left = Node('C')
    tree.root.left.left.left = Node('D')
    tree.root.left.left.left.left = Node('E')
    tree.root.left.left.left.right = Node('F')
    tree.root.left.left.right = Node('G')
    tree.root.left.right = Node('H')
    tree.root.left.right.left = Node('I')
    tree.root.left.right.right = Node('J')
    tree.root.right = Node('K')
    tree.root.right.left = Node('L')
    tree.root.right.right = Node('O')
    tree.root.right.left.left = Node('M')
    tree.root.right.left.right = Node('N')

    print('preorder traversal.....', tree.preorder_trav(tree.root, ""))

    print(height_balanced(tree.root))

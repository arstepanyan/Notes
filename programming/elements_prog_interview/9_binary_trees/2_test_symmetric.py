"""
A binary tree is symmetric if you can draw a vertical line through the root and
then the left subtree is the mirror image of the right subtree

                314
            /        \
          6           6
           \         /
            2       2
             \    /
              3  3

Write a program that checks whether a binary tree is symmetric.
"""


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def symmetric_bt(root):
    return not root or _symmetric_bt(root.left, root.right)


def _symmetric_bt(left, right):
    if not left and not right:
        return True
    elif left and right:
        return (left.value == right.value
                and _symmetric_bt(left.left, right.right)
                and _symmetric_bt(left.right, right.left))
    return False  # One subtree is empty and the other is not


if __name__ == "__main__":
    tree = TreeNode(314)
    tree.left = TreeNode(6)
    tree.left.right = TreeNode(2)
    tree.left.right.right = TreeNode(3)
    tree.right = TreeNode(6)
    tree.right.left = TreeNode(2)
    tree.right.left.left = TreeNode(3)
    print(symmetric_bt((tree)))

    tree = TreeNode(314)
    tree.left = TreeNode(6)
    tree.left.right = TreeNode(2)
    tree.left.right.right = TreeNode(3)
    tree.left.right.right.right = TreeNode(3)
    tree.right = TreeNode(6)
    tree.right.left = TreeNode(2)
    tree.right.left.left = TreeNode(3)
    print(symmetric_bt((tree)))

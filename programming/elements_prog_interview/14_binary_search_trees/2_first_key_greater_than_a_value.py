"""
Write a program that takes as input a BST and a value,
and returns the first key that would appear in an inorder traversal which is greater than the input value.
For example, when applied to the BST bellow, you should return 29 for input 23.

                       19
                    /      \
                  7         43
                /  \       /   \
              3    11     23   47
            / \      \     \     \
           2   5     17     37   53
                     /     /  \
                   13     29  41
                           \
                           31
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# Time = O(h) where h is the height of the tree
# Space = O(1)
def greatest_in_inorder(root, v):
    if not root:
        return None

    while True:
        if root.val <= v:
            if root.right:
                root = root.right
            else:
                return None
        else:  # if root.val > v
            if root.left:
                root = root.left
            else:
                return root.val


if __name__ == "__main__":
    root = TreeNode(19)
    root.left = TreeNode(7)
    root.left.left = TreeNode(3)
    root.left.left.left = TreeNode(2)
    root.left.left.right = TreeNode(5)
    root.left.right = TreeNode(11)
    root.left.right.right = TreeNode(17)
    root.left.right.right.left = TreeNode(13)

    root.right = TreeNode(43)
    root.right.left = TreeNode(23)
    root.right.left.right = TreeNode(37)
    root.right.left.right.left = TreeNode(29)
    root.right.left.right.right = TreeNode(41)
    root.right.left.right.left.right = TreeNode(31)
    root.right.right = TreeNode(47)
    root.right.right.right = TreeNode(53)

    print(greatest_in_inorder(root, 23))

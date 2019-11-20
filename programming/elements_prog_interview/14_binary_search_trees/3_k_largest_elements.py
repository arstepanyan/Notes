"""
Write a program that takes as input a BST and an integer k, and returns the k largest elements in the BST in decreasing order.
For example, if the input is the bellow BST and k=3, your program should return <53, 47, 43>.

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


def k_largest(root, k):
    res = []
    _k_largest(root, res, k)
    return res


def _k_largest(node, res, k):
    if node and len(res) < k:
        _k_largest(node.right, res, k)
        if len(res) < k:
            res.append(node.val)
            _k_largest(node.left, res, k)


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

    print(k_largest(root, 4))

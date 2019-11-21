"""
Design an algorithm that takes as input a BST and two nodes, and returns the LCA (lowest common ancestor) of the two nodes.
For example, for the below BST and nodes with values 3 and 17, your algorithm should return the node with the value 7.
Assume all keys are distinct. Nodes do not have references to their parents.

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
def find_lca(root, node1, node2):
    while root:
        if (node1.val <= root.val and node2.val >= root.val) or (node1.val >= root.val and node2.val <= root.val):
            return root.val
        elif node1.val < root.val and node2.val < root.val:
            root = root.left
        elif node1.val > root.val and node2.val > root.val:
            root = root.right
    return -1


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

    print(find_lca(root, root.left.left, root.left.right.right))
    print(find_lca(root, root.left.left, root.right.left))



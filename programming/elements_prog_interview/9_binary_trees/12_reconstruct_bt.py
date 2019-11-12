"""
Given an inorder traversal sequence and a preorder traversal sequence of a binary tree
write a program to reconstruct the tree. Assume each node has a unique key.

For example, thq unique binary tree whose inorder traversal sequence is <F,B,A,E,H,C,D,I,G>
and whose preorder traversal sequence is <H,B,F,E,A,C,D,G,I> is given bellow.

                     H
                /        \
              B           C
            /  \         / \
          F     E           D
         /\    / \         / \
              A              G
             /\             / \
                          I
                         / \
"""
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, val, left=None, right=None):
        self.root = TreeNode(val, left, right)

    def preorder_traversal(self):
        res = ""
        return self._preorder_traversal(self.root, res)

    def _preorder_traversal(self, node, res):
        if node:
            res += str(node.val) + '-'
            res = self._preorder_traversal(node.left, res)
            res = self._preorder_traversal(node.right, res)
        return res


def recons_tree(inord, preord):
    return _recons_tree(inord, preord, 0)

# Start from the first element of preorder as it is the root of the tree
# Find that element's "index" in the inorder list.
# Set that visited element to None in inorder
# If "index"-1 th element of inorder exists, then there is a left child. That left child is to the right of this element in preorder
# If "index" + 1 th element of inorder exists, then there is a right child.
#     That right child is either 1 (if there is also a left child) or 2 (if there is no left child) step/s to the right of this element in preorder
# If we are done with the left subtree, jump to the right subtree by skipping all of the None elements of the inorder until we reach a non-None element.
# Continue visiting elements and their children recursively
# Stop recursion as soon as both the left and the right elements are set to None in inorder.
#     It will be a leaf
def _recons_tree(inord, preord, i_pre):
    i_in = inord.index(preord[i_pre])

    if (inord[i_in - 1] is None or i_in - 1 not in range(len(inord))) and (inord[i_in + 1] is None or i_in + 1 not in range(len(inord))):
        res, inord[i_in] = inord[i_in], None
        return TreeNode(res, None, None), inord

    inord[i_in], left, right = None, None, None

    # If there is a left child, enter
    if i_in - 1 in range(len(inord)) and inord[i_in - 1] is not None:
        left, inord = _recons_tree(inord, preord, i_pre + 1)

    # If there is a right child, enter
    if i_in + 1 in range(len(inord)) and inord[i_in + 1] is not None:
        # ind will be i_pre + 1 if there is no left child but there is a right child
        # ind will be i_pre + 2 if there are both left and right children
        # ind will jump to the right subtree if we are done with the left subtree
        if left:
            ind = i_pre + 2
            while inord[ind] is None:
                ind += 1
        else:
            ind = i_pre + 1
        right, inord = _recons_tree(inord, preord, ind)

    return TreeNode(preord[i_pre], left, right), inord


if __name__ == "__main__":
    root, inord = recons_tree(inord = ['F', 'B', 'A', 'E', 'H', 'C', 'D', 'I', 'G'],
                              preord = ['H', 'B', 'F', 'E', 'A', 'C', 'D', 'G', 'I'])
    bt = BinaryTree(root.val, root.left, root.right)
    print(bt.preorder_traversal())






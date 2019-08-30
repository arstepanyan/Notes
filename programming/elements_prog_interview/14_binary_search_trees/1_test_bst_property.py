'''
Write a program that takes as input a binary tree and checks if the tree satisfies the BST property
The time complexity is O(n), and the additional space complexity is O(h), where h is the height of the tree.
'''
def check_bst_property(tree):
    if tree is None:
        return True
    if tree.left is not None and tree.data < tree.left:
        return False
    elif tree.right is not None and tree.data > tree.right:
        return False
    else:
        left = check_bst_property(tree.left)
        right = check_bst_property(tree.right)
        return left and right

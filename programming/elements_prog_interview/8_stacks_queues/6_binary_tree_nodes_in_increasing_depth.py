"""
Given a binary tree, return an array consisting of the keys at the same level.
Keys should appear in the order of the corresponding nodes' depths, breaking ties from left to right.
For example, you should return <<314>, <6, 6>, <271, 561, 2, 271>, <28, 0, 3, 1, 28>, <17, 401, 257>, <641>> for the following binary tree

             314
         /         \
        6           6
      /   \       /   \
   271   561     2    271
  /   \    \     \      \
28    0    3      1      28
          /      / \
        17     401 257
                 \
                 641
"""


class TreeNode:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


# Time = O(n), Extra Space = O(n)
def nodes_increasing_depth(root):
    res = []
    if root:
        res.append([root])
    else:
        return res

    while True:
        cur = []
        for el in res[-1]:
            if el.left:
                cur.append(el.left)
            if el.right:
                cur.append(el.right)
        if cur != []:
            res.append(cur)
        else:
            break

    for i in range(len(res)):
        res[i] = [item.data for item in res[i]]
    return res

# Time = O(n), Extra Space = O(m) where m is the maximum number of nodes at any single depth (NOTE: not counting the resulting list)
# Shorter code
def nodes_increasing_depth2(root):
    res = []
    if not root:
        return res

    cur_nodes = [root]
    while True:
        res.append([el.data for el in cur_nodes])
        cur_nodes = [child for cur in cur_nodes for child in (cur.left, cur.right) if child]
        if not cur_nodes:
            break
    return res




if __name__ == "__main__":
    t = TreeNode(314)
    t.left = TreeNode(6)
    t.right = TreeNode(6)
    t.left.left = TreeNode(271)
    t.left.right = TreeNode(561)
    t.left.left.left = TreeNode(28)
    t.left.left.right = TreeNode(0)
    t.left.right.right = TreeNode(3)
    t.left.right.right.left = TreeNode(17)

    t.right = TreeNode(6)
    t.right.left = TreeNode(2)
    t.right.right = TreeNode(271)
    t.right.left.right = TreeNode(1)
    t.right.right.right = TreeNode(28)
    t.right.left.right.left = TreeNode(401)
    t.right.left.right.right = TreeNode(257)
    t.right.left.right.left.right = TreeNode(641)


    print(nodes_increasing_depth(t))



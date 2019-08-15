class Solution(object):
    def binaryTreePaths(self, root):
        """
        Input:
                   1
                 /   \
                2     3
                 \
                  5

        Output: ["1->2->5", "1->3"]
        :type root: TreeNode
        :rtype: List[str]
        """
        res = []
        self._helper(root, res, [])
        return res

    def _helper(self, node, res, buf):
        if not node:
            return res

        buf.append(str(node.val))
        if node.left is None and node.right is None:
            res.append('->'.join(buf))
        else:
            for _node in [node.left, node.right]:
                self._helper(_node, res, buf)
        buf.pop()
        return res
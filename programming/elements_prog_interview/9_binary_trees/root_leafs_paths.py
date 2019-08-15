class Solution(object):
    def paths(self, root):
        """
            Given the root node of a binary tree, return all root-to-leaf paths
            :param node: root node
            :return: list of lists
            """
        res = []
        self._helper(root, res, [])
        return res

    def _helper(self, node, res, buf):
        if not node:
            return res
        buf.append(node.value)
        if not node.left and not node.right:
            res.append(buf.copy())
        else:
            for _node in [node.left, node.right]:
                self._helper(_node, res, buf)
        buf.pop()
        return res
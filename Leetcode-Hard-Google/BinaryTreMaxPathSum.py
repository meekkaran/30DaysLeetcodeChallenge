
class Solution(object):
    def maxPathSum(self, root):
        res = [root.val]
        
        def maxPath(node):
            if not node:
                return 0
            t1 = max(maxPath(node.left), 0)
            t2 = max(maxPath(node.right), 0)
            res[0] = max(res[0], node.val + t1 + t2)
            return max(t1, t2) + node.val
        maxPath(root)
        return res[0]

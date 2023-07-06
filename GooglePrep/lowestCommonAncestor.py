# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        #base cases
        if root is None: return None
        if root.val == p.val: return p
        if root.val == q.val: return q
        #perform dfs on tree
        leftans = self.lowestCommonAncestor(root.left, p, q)
        rightans = self.lowestCommonAncestor(root.right, p,q)
        if leftans == None and rightans == None: return None
        if leftans != None and rightans == None: return leftans
        if leftans == None and rightans != None: return rightans
        return root

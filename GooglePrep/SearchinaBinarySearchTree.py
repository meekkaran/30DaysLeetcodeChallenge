# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        #base case
        if root == None:
            return None
        #travers leftside
        if val < root.val:
            return self.searchBST(root.left,val)
        elif val > root.val:
            return self.searchBST(root.right,val)
        else:
            return root
        return None

                

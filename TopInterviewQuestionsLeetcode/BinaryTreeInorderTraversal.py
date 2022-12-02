# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #O(N) time and O(h) space complexity
        #for each node, traverse from left to root to right
        stack = []  #create nodes array to store nodes
        def inOrder(root):
            if root is None:
                return None
            #visit left
            inOrder(root.left)
            #visit base root
            stack.append(root.val)
            #viit right
            inOrder(root.right)
            
        inOrder(root)
        return stack

    

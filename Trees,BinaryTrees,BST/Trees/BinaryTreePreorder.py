# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #create an empty array to store values of nodes
        stack = []
        def preOrder(root):
            if root is None:
                return None
            #visit root node
            stack.append(root.val)
            #visit left node
            preOrder(root.left)
            #visit right node
            preOrder(root.right)
        
        preOrder(root)
        return stack
    
            
    
        

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        def postOrder(root):
            if root is None:
                return None
            #visit left node
            postOrder(root.left)
            #visit right node
            postOrder(root.right)
            #visit root node
            stack.append(root.val)
        postOrder(root)
        return stack
        

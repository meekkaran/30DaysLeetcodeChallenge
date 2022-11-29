# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        totalNums = len(nums)
        if not totalNums: return None
        
        #find the midpoint
        midNode = totalNums // 2
        
        return TreeNode( nums[midNode], self.sortedArrayToBST(nums[:midNode]), self.sortedArrayToBST(nums[midNode+1:]));
    
    # time complexity o(log)n
    # space complexity o(n)
        
        

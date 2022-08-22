# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        #the root node is the midpoint
        #create a unction --- recursion
        def arrayToTree( l,r):
            if l > r: return None
            if l == r: return TreeNode(nums[l])
            mid = (l+r)//2
            left = arrayToTree(l,mid -1)
            right = arrayToTree(mid + 1 ,r)
            root = TreeNode(nums[mid])
            root.left = left
            root.right = right
            return root
        ans = arrayToTree(0,len(nums)-1)
        return ans

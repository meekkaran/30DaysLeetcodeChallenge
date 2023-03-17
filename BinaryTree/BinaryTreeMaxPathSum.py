# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        results = [float("-inf")]
        self.findMaxSum(root, results)
        return results[0] if results[0] != float("inf") else -1

    def findMaxSum(self,node,results):
        if node is None: return 0
        leftBranch = self.findMaxSum(node.left, results)
        rightBranch = self.findMaxSum(node.right, results)

        value = node.val

        maxSumBranch = max(max(leftBranch,rightBranch) +value, value)
        maxRootSum = max(maxSumBranch, leftBranch + rightBranch + value)

        results[0] = max(results[0], maxRootSum)
        return maxSumBranch

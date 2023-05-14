#kadane algorithm
#O(n) time and O(1)space
class Solution(object):
    def maxSubArray(self, nums):
        currSum = 0
        maxSum = nums[0]
        
        for n in nums:
            if currSum < 0:
                currSum = 0
            currSum += n
            maxSum = max(currSum, maxSum)
        return maxSum




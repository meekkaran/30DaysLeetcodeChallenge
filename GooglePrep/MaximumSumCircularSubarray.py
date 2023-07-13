class Solution(object):
    def maxSubarraySumCircular(self, nums):
        #O(n) time O(1)space
        currMax = 0
        currMin = 0
        globMax = nums[0]
        globMin = nums[0]
        total = 0
        for n in nums:
            currMax = max(currMax + n, n)
            currMin = min(currMin + n, n)
            total += n
            globMax = max(globMax, currMax)
            globMin = min(globMin, currMin)
        return max(globMax, total - globMin) if globMax > 0 else globMax

        

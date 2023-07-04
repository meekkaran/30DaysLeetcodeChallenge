class Solution(object):
    def maxProduct(self, nums):
        #O(n) time and O(1)space
        #dynamic programming
        #at each index, find max and min product
        maxprod = nums[0]
        minprod = nums[0]
        ans = nums[0]

        for i in range(1, len(nums)):
            x = max(nums[i], maxprod * nums[i], minprod * nums[i])
            y = min(nums[i], maxprod * nums[i], minprod * nums[i])
            maxprod = x
            minprod = y
            ans = max(maxprod , ans)
        return ans

        

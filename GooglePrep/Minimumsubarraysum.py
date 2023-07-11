class Solution(object):
    def minSubArrayLen(self, target, nums):
        #O(n) time and O(1)space - sliding window
        #return min length of subarray whose length >= target else 0
        i = 0
        sums = 0
        min_length = float('inf')

        for j in range(len(nums)):
            sums += nums[j]

            while sums >= target:
                min_length = min(min_length, j - i + 1) #length
                sums -= nums[i]
                i += 1
        return min_length if min_length != float('inf') else 0

              

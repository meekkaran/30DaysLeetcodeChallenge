class Solution(object):
    def missingNumber(self, nums):
        N = len(nums)
        actualSum = sum(nums)
        expectedSum = N *(N + 1) // 2

        sums = expectedSum - actualSum
        return sums

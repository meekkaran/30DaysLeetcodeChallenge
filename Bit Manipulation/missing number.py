class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        N  = len(nums)
        ExpectedSum = N*(N+1)//2
        ActualSum = sum(nums)
        return ExpectedSum - ActualSum

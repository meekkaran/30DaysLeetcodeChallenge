class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #using o(n) time and O(1) space
        c = Counter(nums)
        N = len(nums)
        for i in range(N + 1):
            if i not in c:
                return i
        
        ##step 2 ; math formula
        #using o(n) time and 0(1) space
        N = len(nums)
        ExpSum = N*(N+1)//2
        ActualSum = sum(nums)
        return ExpSum - ActualSum

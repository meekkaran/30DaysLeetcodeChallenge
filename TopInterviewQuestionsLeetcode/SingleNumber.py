class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #O(N) time and O(1) space
        #use counter function
        c = Counter(nums)
        for num in nums:
            if c[num] == 1:
                return num
          
        

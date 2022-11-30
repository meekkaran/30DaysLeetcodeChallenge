class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        res = Counter(nums)
        for i in nums:
            if res[i] > 1:
                return True
        return False
    
                
        

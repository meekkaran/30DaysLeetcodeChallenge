class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        #a set stres unique elements
        for i in nums:
            if i in seen:# if the number is in a set already, that means its duplicate
                return True
            else:
                seen.add(i)
        return False
                

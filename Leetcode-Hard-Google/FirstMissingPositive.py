#o(n) time and O(1) space
class Solution(object):
    def firstMissingPositive(self, nums):
        #the smallest +ve int should def be 1 
        i = 1
        seen = set(nums)
        #if one is in nums then the smallest +ve could be 2 or 3 or ...
        while i in seen:
            i += 1
        return i
        

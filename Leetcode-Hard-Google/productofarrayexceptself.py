#O(n) time and space
class Solution(object):
    def productExceptSelf(self, nums):
        #calculate product of each int to the left and to its right
        n = len(nums)
        result = [1] * n
        #calculate product of each eement to its left
        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]
        
        #calculate product on each element to its right and update result 
        postfix = 1
        for i in range(n-1, -1,-1):
            result[i] *= postfix
            postfix *= nums[i]
        return result                                                                     
        
        
        
        

class Solution(object):
    def rob(self, nums):
        #O(n) time and O(1)space
        #perform nouse robber1 sln but , ignore the first and last value in nums
        #create a haelper fn to calculate house robber
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))
    
    def helper(self, nums):
        rob1, rob2 = 0 ,0
        for n in nums:
            newRob = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = newRob
        return rob2

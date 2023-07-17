class Solution(object):
    #O(n)time O(1) space
    def rob(self, nums):
        #come up with 2 variables
        rob1, rob2 = 0,0

        for n in nums:
            #you only need sum of adjacent so if its not rob2, its rob1 + n
            newRob = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = newRob
        return rob2  

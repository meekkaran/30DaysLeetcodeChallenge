#O(n)time and space
class Solution(object):
    def subsets(self, nums):
        output = [[]]
        for i in nums:
            output += [o + [i] for o in output]
        return output

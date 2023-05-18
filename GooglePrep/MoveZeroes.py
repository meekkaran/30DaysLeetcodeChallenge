#o(n) time and O(1)space
class Solution(object):
    def moveZeroes(self, nums):
        anchor = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[anchor],nums[i] = nums[i], nums[anchor]
                anchor += 1

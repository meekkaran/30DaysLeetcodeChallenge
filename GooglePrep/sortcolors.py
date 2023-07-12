class Solution(object):
    def sortColors(self, nums):
        #0(n) time and O(1)space
        #have 3 pointers - dutch flag algorithm
        low = 0
        mid = 0
        high  = len(nums) -1
        while mid <= high:
            if nums[mid] == 0:
                nums[low],nums[mid] = nums[mid],nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid],nums[high] = nums[high], nums[mid]
                high -= 1




                

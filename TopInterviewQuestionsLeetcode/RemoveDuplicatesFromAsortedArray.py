class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #O(1) space and O(n) time
        #have two pointers
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[j -1]:
                nums[i] = nums[j-1]
                i += 1
        nums[i] = nums[-1]
        return i + 1

    
  ###solution 2
class Solution(object):
    def removeDuplicates(self, nums):
        #since we need o(1) space, use two pointers
        #O(N) time and O(1) space
        leftp = 1
        for rightp in range(1, len(nums)):
            if nums[rightp] != nums[rightp - 1]:
                nums[leftp] = nums[rightp]
                leftp += 1
        return leftp
            
                

        
        

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

            
                

        
        

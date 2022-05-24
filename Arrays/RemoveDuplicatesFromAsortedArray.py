class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #leftpointer will show where to put the next unique value
        #rightpointer will scan through the array
        #initialise the two pointers on the second value, the firt value is taken as the first unique value
        l = 1
        for r in range(1,len(nums)):
            if nums[r]!= nums[r-1]:
                nums[l]=nums[r]
                l+=1
        return l

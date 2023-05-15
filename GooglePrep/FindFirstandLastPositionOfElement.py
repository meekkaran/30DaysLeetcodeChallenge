#O(log(n)) time and O(1)space
#run 2 bs , one for the 1st edx and another for end idx
class Solution(object):
    def searchRange(self, nums, target):  
        ans = [-1, -1] #to update result
        #bs 1
        l,r = 0, len(nums) -1
        while l <= r:
            mid = (l+r)//2
            if target == nums[mid]:
                ans[0] = mid
                r = mid - 1
            elif target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        #bs 2
        l,r = 0, len(nums) -1
        while l <= r:
            mid = (l+r)//2
            if target == nums[mid]:
                ans[1] = mid
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        return ans
                

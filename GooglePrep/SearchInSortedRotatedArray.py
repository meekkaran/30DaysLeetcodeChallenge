#O(log(n)) time and O(1)space
class Solution(object):
    def search(self, nums, target):
        l = 0
        r = len(nums) -1

        while l <= r:
            mid = (l + r)//2
            if target == nums[mid]:
                return mid
            elif nums[0] <= target < nums[mid] or target < nums[mid] < nums[0] or nums[mid] < nums[0] <= target:
                r = mid - 1
            else:
                l = mid + 1
        return -1

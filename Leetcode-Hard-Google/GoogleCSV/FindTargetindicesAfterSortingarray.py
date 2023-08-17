#O(n(log(n)) time and O(n) space
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        res = [] #to add final output
        #sort array
        nums.sort()
        #find targwt indices in the sorted arr
        for i in range (len(nums)):
            if nums[i] == target:
                res.append(i)
        return res


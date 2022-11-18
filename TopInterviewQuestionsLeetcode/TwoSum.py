class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #brute-force approach
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        
        #use of hashmap
        seen = {}
        for i,value in enumerate(nums):
            rem = target - nums[i]
            if rem in seen:
                return [seen[rem],i]
            seen[value] = i
                

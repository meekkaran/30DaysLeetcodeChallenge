class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # brute-force solution
        # time complexity 0(n)2
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums [j] == target:
                    return [i,j]
        return false
        
        # using a hashtable 
        hashtable = {}
        for i in range(len(nums)):
            # if i is in  the hashtable
            if nums[i] in hashtable:
                return [hashtable[nums[i]] ,i]
            # if i not, add hashtable 
            else:
                hashtable[target-nums[i]] = i
        return None
                     

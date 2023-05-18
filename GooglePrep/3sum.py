#O(N(log(n))) time due to sorting and O(1)space
class Solution(object):
    def threeSum(self, nums):
        ans = set() #for final output
        nums.sort()
        n = len(nums)
        for i in range(n):
            j = i + 1
            k = n - 1
            while j <=k:
                s = nums[i] + nums[j] + nums[k]
                if i!=j and i !=k and j!=k and s == 0:
                    ans.add((nums[i],nums[j],nums[k]))
                    j += 1
                    k -= 1
                elif s > 0:
                    k -= 1
                else:
                    j += 1
        return ans


       
                

#O(n(logN)) time and O(n) space
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #longest increasing subsequence
        sub = []
        for x in nums:
            if len(sub) == 0 or sub[-1] < x:
                sub.append(x)
            else:
                idx = bisect_left(sub,x) #find idx of first element thats >= x
                sub[idx] = x
        return len(sub)

#O(N^2) time and O(n) space
class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        #divide into two groups, then calculate sum of group 1 in hashmap then group 2
        n = len(nums1)
        ans = 0
        hashmap = {}
        for a in range(n):
            for b in range(n):
                if nums1[a] + nums2[b] not in hashmap:
                    hashmap[nums1[a]+nums2[b]] = 1
                else:
                    hashmap[nums1[a]+nums2[b]] += 1
        for a in range(n):
            for b in range(n):
                if 0-(nums3[a] + nums4[b]) in hashmap:
                    ans += hashmap[0 - (nums3[a] + nums4[b])]
        return ans
                    
        
        

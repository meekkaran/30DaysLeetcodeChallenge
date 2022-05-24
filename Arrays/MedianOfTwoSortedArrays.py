class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # step1: merge the two arrays and sort them
        x = sorted(nums1+nums2)
        print(x)
        n = len(x)
        if n%2 != 0:#odd
            return x[n//2]
        else:#even
            return (x[n//2] + x[(n-1)//2])/2.0
        

#O(log(N-K)+k) time and O(1)space
class Solution(object):
    def findClosestElements(self, arr, k, x):
        #find midpoint between left upto k
        l = 0
        r = len(arr) - k
        mid = (l + r) //2
        while l < r:
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                r = mid
        return arr[l:l+k] 

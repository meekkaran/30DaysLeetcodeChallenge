class Solution:
    def mySqrt(self, x: int) -> int:
        #binary search
        #time O(logN) | space O(1)
        low = 1
        high  = x
        ans = 0
        
        while low <= high:
            mid = (low + high)//2
            sqrt = mid * mid
            if sqrt == x:
                return mid
            elif sqrt < x:
                low = mid + 1
                ans = mid
            else:
                high = mid - 1
        return ans

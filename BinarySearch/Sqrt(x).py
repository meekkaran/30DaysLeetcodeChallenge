class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 and x == 1:
            return x
        start = 1
        end = x
        ans = 0
        while start <= end:
            midpoint = (start + end)//2
            if midpoint * midpoint == x:
                return midpoint
            if midpoint * midpoint < x:
                start = midpoint + 1
                ans = midpoint
            else:
                end = midpoint - 1
        return ans 
 

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # a no. is a power of 3 if recursively divided by 3 gives 1
        # a no. is a power of 3 if its an off no and not less than 0
        if n <= 0:
            return False
        if n == 1:
            return True
        return n % 3 == 0 and self.isPowerOfThree(n/3)
        
        #solution2 - 
        if n <= 0:
            return False
        if n == 1:
            return True
        while n % 3 == 0:
            n /= 3
        return n == 1

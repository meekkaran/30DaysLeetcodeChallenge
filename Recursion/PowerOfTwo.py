class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        #a no. is apower of two if if recursively divideb by 2 ==1
        #if a no. is 0 or not divisible by 2; return false
        if n == 0 : return False
        if n == 1 :return True
        return n % 2 == 0 and self.isPowerOfTwo(n//2)
    #o(log)n time and space complexity
        

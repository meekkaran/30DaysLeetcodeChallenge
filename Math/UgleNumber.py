class Solution:
    def isUgly(self, n: int) -> bool:
        #base case 
        if n <= 0:
            return 0
        #if the no. is related to 2,3 or 5
        #prime factors*****
        for p in [2,3,5]:
            #while n is divisible by either 2 or 3 or 5
            #i.e if n is divisible by 2, then lets divide it by 2
            while n % p == 0:
                n = n // p
        #return true if n == 1
        return n == 1

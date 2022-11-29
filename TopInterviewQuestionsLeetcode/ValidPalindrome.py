class Solution:
    def isPalindrome(self, s: str) -> bool:
        #isalpha() and isnumeric() are python functions to check if str is numeric or alphabet
        #time and space complexity O(N)
        a = ""
        for x in s:
            if x.isalpha(): 
                a += x.lower()
            if x.isnumeric():
                a += x
        return a == a[::-1]

            

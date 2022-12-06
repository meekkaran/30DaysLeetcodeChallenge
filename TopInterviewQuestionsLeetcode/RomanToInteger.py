class Solution:
    def romanToInt(self, s: str) -> int:
        #O(n) time and O(n) space complexity
        lookup = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }   

        N = len(s)
        i  = N - 1 #initiate a pointer at thene dof the string
        output = 0
        #itierate from the end to the begining, 
        while i >= 0:
            if i < N - 1 and lookup[s[i]] < lookup[s[i+1]]:
                 output -= lookup[s[i]]
            else:
                output += lookup[s[i]]
            i -= 1
        return output
        
            
                
            

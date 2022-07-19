class Solution:
    def romanToInt(self, s: str) -> int:
        lookup = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
        }
        # start from the end to the beginning
        N = len(s)
        i = N-1 #initialise a pointer at the end of the len(s)
        output = 0
        while i >= 0:
            # if its less than the no. after, subtract , else add 
            if i< N-1 and lookup[s[i]] < lookup[s[i+1]]:
                output -= lookup[s[i]]
            else:
                output += lookup[s[i]]
            i -= 1
        return output

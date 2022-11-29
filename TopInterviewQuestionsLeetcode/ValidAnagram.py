class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #base case
        if len(s) != len(t):
            return False
        l = "abcdefghijklmnopqrstuvwxyz"
        for char in l:
            if s.count(char) != t.count(char):
                return False
        return True
        
        if len(s) != len(t):
            return False
        if sorted(s) == sorted(t):
            return True
        else:
            return False

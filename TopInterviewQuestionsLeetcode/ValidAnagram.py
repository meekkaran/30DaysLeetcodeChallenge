class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #solution1
        #base case
        if len(s) != len(t):
            return False
        l = "abcdefghijklmnopqrstuvwxyz"
        for char in l:
            if s.count(char) != t.count(char):
                return False
        return True
        
        
        #solution2
        if len(s) != len(t):
            return False
        if sorted(s) == sorted(t):
            return True
        else:
            return False
        
      ## O(n) time and space

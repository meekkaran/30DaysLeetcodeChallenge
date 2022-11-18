class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        result = 0
        #initialise two pointers
        l = 0
        for r in range(len(s)):
            while s[r] in charSet: #meaning their is a duplicate value
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            
            result = max(result, r -l + 1)
        return result
                
        

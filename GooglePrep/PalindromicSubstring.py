#O(n^2) time and O(n) space
class Solution(object):
    def countSubstrings(self, s):
        #find both even and odd strings
        res = 0
        
        for i in range(len(s)):
            #odd string
            l = r = i
            while l >= 0 and r < len(s) and s[l]== s[r]:
                res += 1
                l -= 1
                r += 1
            #even string
            l = i
            r =  i + 1
            while l >= 0 and r < len(s) and s[l]== s[r]:
                res += 1
                l -= 1
                r += 1
        return res

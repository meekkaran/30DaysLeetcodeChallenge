class Solution:
    def romanToInt(self, s: str) -> int:
        map = {'I':1, 'V':5, 'X':10,'L':50,'C':100,'D':500,'M':1000}
        n = len(s)
        #create a variable num that will store results
        num = map[s[n-1]];
        #loop for each character from right to left
        for i in range (n-2, -1, -1):
            if map[s[i]] > map[s[i+1]] or map[s[i]] == map[s[i+1]]:
                num += map[s[i]]
            else:
                num -= map[s[i]]
        return num
             

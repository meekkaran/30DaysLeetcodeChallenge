class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        #base case
        if len(p) > len(s): return []
        #create two hashmaps to store key/value for comparison
        pCount = {}
        sCount = {}
        #iterate through s, with the p's length
        #sliding window initiaised
        for i in range(len(p)):
            pCount[p[i]] = 1 + pCount.get(p[i], 0)
            sCount[s[i]] = 1 + sCount.get(s[i], 0)
            
            #if 2 hashmaps are equal, insert index 0
        res = [0] if sCount == pCount else []
        
        #create two pointers ,add each right pointer to the hashmap
        l = 0
        for r in range(len(p),len(s)):
            sCount[s[r]] = 1 + sCount.get(s[r] ,0) #add the value at right pointer to hashmap
            sCount[s[l]] -= 1  #remove the char at the left pointer
            
            #if count of char is 0, remove it from the hashmap
            if sCount[s[l]] == 0:
                sCount.pop(s[l])
            l +=1
            if sCount == pCount:
                res.append(l) #this is the first digit
        return res
                
                
            
        
        

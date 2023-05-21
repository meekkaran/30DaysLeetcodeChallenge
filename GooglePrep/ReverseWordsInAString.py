#O(n) time and O(1)space
class Solution(object):
    def reverseWords(self, s):
        newStr = s.split() #convert to int
        newStr.reverse() #reverse it  #O(n) time 
        finalStr = ' '.join(newStr) #convert back to string
        return finalStr

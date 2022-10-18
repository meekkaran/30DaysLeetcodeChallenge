class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        if x < 0:
            sign = -1
        xabs = abs(x) # get asolute value
        xstr = str(xabs)# convert to str
        xlen = len(xstr)-1# get last index 
        y = ""
        while xlen >= 0:
            if xstr[xlen] != 0:
                y += xstr[xlen]
                xlen -= 1
        if int(y) > 2147483647:
            return 0
        y = int(y) * sign
        return y
        
        
        
        
        
        
        
        
        
        
  
        
        
        
        
   

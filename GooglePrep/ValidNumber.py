#O(n) time and O(1)space
class Solution(object):
    def isNumber(self, s):
        #four checks to clarify validity
        num, exp, sign, dec = False, False, False, False

        for c in s:
            #number
            if c >='0' and c <='9':
                num = True
            #exponential
            elif c == 'e' or c == 'E':
                if exp or not num:
                    return False
                else:
                    exp, num, sign, dec = True,False,False,False
            #sign
            elif c == '+' or c == '-':
                if sign or num or dec:
                    return False
                else:
                    sign = True
            #decimal
            elif c == '.':
                if dec or exp:
                    return False
                else:
                    dec = True
            else:
                return False
        return num
        

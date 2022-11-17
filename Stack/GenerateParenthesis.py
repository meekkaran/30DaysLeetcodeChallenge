class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        
        def backtrack(leftP,rightP):
            #if l ,r ,n is equal
            if leftP == rightP == n:
                res.append("".join(stack))
                return
            
            if leftP < n:
                stack.append("(")
                backtrack(leftP +1,rightP)
                stack.pop()
                
            if rightP < leftP:
                stack.append(")")
                backtrack(leftP,rightP+1)
                stack.pop()
                
        backtrack(0,0)
        return res
        

                
            
            

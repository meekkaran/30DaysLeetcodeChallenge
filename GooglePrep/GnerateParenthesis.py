#O(2^n) time and O(n)space
class Solution(object):
    def generateParenthesis(self, n):
        res = [] #to store final output
        stack = [] #to store curr paranthesis

        def backtrack(leftP, rightP):
            if leftP == rightP == n:
                res.append("".join(stack))
            if leftP < n:
                stack.append("(")
                backtrack(leftP + 1, rightP)
                stack.pop()
            if rightP < leftP:
                stack.append(")")
                backtrack(leftP, rightP +1)
                stack.pop()
        backtrack(0,0)
        return res

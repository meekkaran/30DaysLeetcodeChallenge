class Solution:
    def isValid(self, s: str) -> bool:
        mappings = { "(":")","[":"]","{":"}" }
        
        stack = []
        for char in s:
            if char in mappings:
                stack.append(mappings[char])
            elif not stack or stack[-1] != char:
                return False
            else:
                stack.pop()
        return len(stack) == 0
            
            

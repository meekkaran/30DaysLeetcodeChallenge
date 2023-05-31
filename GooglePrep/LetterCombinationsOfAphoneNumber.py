#O(n) time and space
class Solution(object):
    def letterCombinations(self, digits):
        lookup = {"2": "abc",
                  "3": "def",
                  "4": "ghi", 
                  "5": "jkl", 
                  "6": "mno", 
                  "7": "pqrs", 
                  "8": "tuv", 
                  "9": "wxyz"}
        if not digits: return []
        output = []
        def backtrack(combination, next_digits):
            if not next_digits:#if there a re no more digits to process, append to final list
                output.append(combination)
                return
            
            for letter in lookup[next_digits[0]]:
                backtrack(combination + letter, next_digits[1:])
        backtrack("", digits)
        return output
        


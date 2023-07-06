class Solution(object):
    #O(n^2*m) time | O(n)space
    def wordBreak(self, s, wordDict):
        dp = [False] * (len(s) +1)
        dp[0] = True
        for i in range(1, len(s) +1):
            for word in wordDict:
                if len(word) > i:
                    continue
                if s[i - len(word):i] == word and dp[i - len(word)]:
                    dp[i] = dp[i - len(word)]
                    break
        return dp[len(s)]

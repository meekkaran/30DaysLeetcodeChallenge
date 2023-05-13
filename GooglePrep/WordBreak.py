#O(n^2 +m) time and O(n)space
class Solution(object):
    def wordBreak(self, s, wordDict):
        #DP with bottom-up
        dp = [False] * (len(s) +1)
        dp[0] = True
        for i in range(1, len(s) +1):
            #iterate word in worddict that iterating from 0 to i
            for word in wordDict:
                if len(word) > i:
                    continue
                if s[i - len(word):i] == word and dp[i - len(word)]:
                    dp[i] = dp[i - len(word)]
                    break
        return dp[len(s)]

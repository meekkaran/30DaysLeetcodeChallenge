#O(n) time and space
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        m = len(text1)
        n = len(text2)

        ans = 0
        dp = [[0 for i in range(n+1)] for j in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max((dp[i][j-1]), (dp[i-1][j]))
                ans = max(ans, dp[i][j])
        return ans

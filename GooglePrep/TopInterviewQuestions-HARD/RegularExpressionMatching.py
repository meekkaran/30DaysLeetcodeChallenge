class Solution(object):
    def isMatch(self, s, p):
        #O(M*N) time and space complexity 
        #match a pettern p with string s
        #there are 2 conditions: . = any single char whie * = 0 or preceding chars
        #make sure i cater for the above
        m = len(s)
        n = len(p)
        
        dp = [[False] * (n+1) for _ in range(m+1)] #define a dp
        dp[0][0] = True #(an empty pattern matches an empty string)

        #consider first row of dp matrix,
        #if first pattern of p starts with".", then it can match zero occurences
        for j in range(1, n+1):
            if p[j-1] == "*" :
                dp[0][j] = dp[0][j-2]

        #fill in remaining cells
        for i in range(1, m+1):
            for j in range(1, n+1):
                #based on two previous conditions
                #cond - . to represent any single char
                if s[i-1] == p[j-1] or p[j-1] == '.':
                    dp[i][j] = dp[i-1][j-1]
                #cond - * that has two cases
                #two conditions, either 0 occurences or preceding chars
                # if dp[i][j-2]
                elif p[j-1] == "*":
                    dp[i][j] = dp[i][j-2]
                    if s[i-1] == p[j-2] or p[j-2] == '.':
                        dp[i][j] = dp[i-1][j]
        return dp[m][n]

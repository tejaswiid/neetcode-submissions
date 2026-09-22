class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {}
        dp[len(s)] = 1

        def dfs(i):
            if i in dp: return dp[i]
            if int(s[i]) == 0:
                return 0
            
            dp[i] = 0
            dp[i] += dfs(i+1)
            if i+2 <= len(s) and int(s[i:i+2]) < 27:
                dp[i] += dfs(i+2)
            return dp[i]
        return dfs(0)

        
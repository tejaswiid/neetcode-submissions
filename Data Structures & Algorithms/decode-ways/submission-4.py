class Solution:
    def numDecodings(self, s: str) -> int:
        new = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        dp = {}

        def dfs(i):
            if i >= len(s):
                return 1
            if i in dp: return dp[i]
            if s[i] == "0":
                return 0
            dp[i] = dfs(i+1)
            if i+1 < len(s) and int(s[i]) <= 2:
                if int(s[i]) == 1:
                    dp[i] += dfs(i+2)
                elif int(s[i]) == 2 and int(s[i+1]) <= 6:
                    dp[i] += dfs(i+2)
            return dp[i]
        return dfs(0)
        

                
        
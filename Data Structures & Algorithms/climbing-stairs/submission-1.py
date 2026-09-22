class Solution:
    def climbStairs(self, n: int) -> int:
        self.res = 0
        dp = {}
        dp[n] = 1
        dp[n+1] = 0
        def dfs(i):
            if i in dp:
                return dp[i]
            dp[i] = dfs(i+1) + dfs(i+2)
            
            return dp[i]
        dfs(0)
        return dp[0]


        
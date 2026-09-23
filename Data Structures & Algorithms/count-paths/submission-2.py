class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        dp[0][0] = 1
        def dfs(i,j):
            if dp[i][j] != -1: return dp[i][j]
            dp[i][j] = 0
            if i-1 >= 0:
                dp[i][j] = dfs(i-1,j) 
            if j-1 >= 0:
                dp[i][j]+= dfs(i,j-1)
            return dp[i][j]
        return dfs(m-1,n-1)

        
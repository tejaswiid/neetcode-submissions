class Solution:
    def integerBreak(self, num: int) -> int:
        dp = {1:1}
        def dfs(n):
            if n in dp: return dp[n]
            res = 0 if n == num else n
            for i in range(1,n):
                val = dfs(i) * dfs(n-i)
                res = max(res,val)
            dp[n] = res
            return res
        return dfs(num)

        
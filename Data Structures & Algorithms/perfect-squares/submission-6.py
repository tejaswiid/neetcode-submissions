class Solution:
    def numSquares(self, n: int) -> int:
        perf = []
        def gen(n):
            i = 1
            while i*i <= n:
                perf.append(i*i)
                i += 1
        gen(n)
        perf = perf[::-1]
        dp = [-1]*(n+1)
        dp[n] = 0
        def dfs(val):
            if dp[val] != -1: return dp[val]
            new = float("inf")
            for p in perf:
                if val + p > n:
                    continue
                val += p
                new = min(new,1 + dfs(val))
                val -= p
            dp[val] = new
            return new 
        dfs(0)
        return dp[0]

      
                
    
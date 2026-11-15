class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[-1 for _ in range(n)] for _ in range(n)]
        def dfs(l,r):
            if l >= r:
                dp[l][r] = True
                return True
            if dp[l][r] != -1: return dp[l][r]
            dp[l][r] = False
            if s[l] == s[r]:
                dp[l][r] = dfs(l+1,r-1)
            return dp[l][r]
        res = 0
        for l in range(n):
            for r in range(l,n):
                if dfs(l,r):
                    res += 1
        return res

            
        
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
  
        dp = {}
        def dfs(i,j):
            if j == len(t):
                return 1
            if i == len(s): return 0
            if (i,j) in dp: return dp[(i,j)]
            val = 0
            if s[i] == t[j]:
                val += dfs(i+1,j+1)
            val += dfs(i+1,j)
            dp[(i,j)] = val
            return val
        return dfs(0,0)


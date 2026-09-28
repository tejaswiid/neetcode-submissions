class Solution:
    def numDistinct(self, s: str, t: str) -> int:
  
        dp = {}
        def dfs(i,j):
            if i == len(s):
                if j == len(t):
                    return 1
                return 0
            if (i,j) in dp: return dp[(i,j)]
            dp[(i,j)] = 0
            if j < len(t) and s[i] == t[j]:
                dp[(i,j)] += dfs(i+1,j+1)
            dp[(i,j)] += dfs(i+1,j)
            return dp[(i,j)]
        return dfs(0,0)
            
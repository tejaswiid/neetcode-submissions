class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = {(m-1,n-1):1}
        
        def dfs(i,j):
            if (i,j) in dp: return dp[(i,j)]
            res = 0
            if i+1 < m:
                res += dfs(i+1,j) 
            if j+1 < n:
                res += dfs(i,j+1)
            dp[(i,j)] = res
            return res
        return dfs(0,0)
            
        
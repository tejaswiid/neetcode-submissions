class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = {(m-1,n-1):grid[m-1][n-1]}
        def dfs(r,c):
            if (r,c) in dp: return dp[(r,c)]
            res = grid[r][c]
            if r+1 < m and c+1 < n:
                res += min(dfs(r+1,c), dfs(r,c+1))
            elif r+1 < m:
                res += dfs(r+1,c)
            else:
                res +=  dfs(r,c+1)
            dp[(r,c)] = res
            return res
        return dfs(0,0)
    
                
            
            
        
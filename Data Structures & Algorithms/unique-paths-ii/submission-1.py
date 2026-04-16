class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1: return 0
        m, n = len(grid), len(grid[0])
        dp = {(m-1,n-1):1}
        def dfs(r,c):
            if (r,c) in dp: return dp[(r,c)]
            res = 0
            if r + 1 < m and grid[r+1][c] == 0:
                res += dfs(r+1,c)
            if c + 1 < n and grid[r][c+1] == 0:
                res += dfs(r,c+1)
            dp[(r,c)] = res
            return res

        return dfs(0,0)

        
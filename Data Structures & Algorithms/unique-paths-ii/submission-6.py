class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        if grid[0][0] == 1: return 0
        dp = {(rows-1,cols-1):1}
        def dfs(i,j):
            if (i,j) in dp: return dp[(i,j)]
            res = 0
            if i+1 < rows and grid[i+1][j] != 1:
                res += dfs(i+1,j)
            if j+1 < cols and grid[i][j+1] != 1:
                res += dfs(i,j+1)
            dp[(i,j)] = res
            return res
        return dfs(0,0)

        
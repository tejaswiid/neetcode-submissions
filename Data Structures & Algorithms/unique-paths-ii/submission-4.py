class Solution:
    def uniquePathsWithObstacles(self,grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dp = {}
        if grid[rows-1][cols-1] == 1: return 0
        dp[(rows-1,cols-1)] = 1
        def dfs(r,c):
            if (r,c) in dp: return dp[(r,c)]
            if r >= rows or c >= cols:
                return 0
            if grid[r][c] == 1:
                dp[(r,c)] = 0
                return 0
            down = dfs(r+1,c)
            right = dfs(r,c+1)
            dp[(r,c)] = down+right
            return dp[(r,c)]
        return dfs(0,0)

        
        
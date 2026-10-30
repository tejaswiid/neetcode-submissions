class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dp = {}
        dp[(rows-1,cols-1)] = grid[-1][-1]
        def dfs(r,c):
            if (r,c) in dp: return dp[(r,c)]
            if r >= rows or c >= cols:
                return float("inf")
            su = grid[r][c] 
            down = dfs(r+1,c)
            right = dfs(r,c+1)
            dp[(r,c)] = su+min(down,right)
            return dp[(r,c)]
        return dfs(0,0)


        
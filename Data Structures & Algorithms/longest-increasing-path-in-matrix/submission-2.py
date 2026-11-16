class Solution:
    def longestIncreasingPath(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dp = [[-1 for _ in range(cols)] for _ in range(rows)]
        dirs = [[0,1],[1,0],[0,-1],[-1,0]]
        def dfs(r,c):
            if dp[r][c] != -1: return dp[r][c]
            res = 0
            for dr,dc in dirs:
                rr, cc = r+dr, c+dc
                if rr in range(rows) and cc in range(cols):
                    if grid[rr][cc] > grid[r][c]:
                        res = max(res,1+dfs(rr,cc))
            dp[r][c] = res
            return res
        for r in range(rows):
            for c in range(cols):
                if dp[r][c] == -1:
                    dfs(r,c)
        res = 0
        print(dp)
        for r in range(rows):
            res = max(res,max(dp[r]))
        return res+1

            

        
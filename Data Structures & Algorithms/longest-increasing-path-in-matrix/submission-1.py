class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dp = {}
        def dfs(i,j):
            dirs = [[0,1],[1,0],[-1,0],[0,-1]]
            if (i,j) in dp: return dp[(i,j)]
            dp[(i,j)] = 1
            for dr,dc in dirs:
                rr, cc = i+dr, j+dc
                if rr in range(rows) and cc in range(cols):
                    if matrix[rr][cc] > matrix[i][j]:
                        dp[(i,j)] = max(dp[(i,j)], 1 + dfs(rr,cc))
            return dp[(i,j)]
        ans = 0 
        for r in range(rows):
            for c in range(cols):
                ans = max(ans,dfs(r,c))
        return ans


                    
        
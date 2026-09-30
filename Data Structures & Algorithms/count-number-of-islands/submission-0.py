class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit = set()
        rows, cols = len(grid), len(grid[0])
        dirs = [[0,1],[1,0],[0,-1],[-1,0]]
        def bfs(i,j):
            q = deque()
            q.append((i,j))
            while q:
                r,c = q.popleft()
                for dr,dc in dirs:
                    rr, cc = r+dr, c+dc
                    if rr in range(rows) and cc in range(cols) and (rr,cc) not in visit and grid[rr][cc] == "1":
                        visit.add((rr,cc))
                        q.append((rr,cc))
            return 
        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    res += 1
                    visit.add((r,c))
                    bfs(r,c)
        return res
            


        
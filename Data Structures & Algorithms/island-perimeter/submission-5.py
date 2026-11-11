class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visit = set()
        self.res = 0
        def bfs(r,c):
            q = deque()
            q.append((r,c))
            visit.add((r,c))
            dirs = [[0,1],[1,0],[-1,0],[0,-1]]
            while q:
                r,c = q.popleft()
                for dr,dc in dirs:
                    rr, cc = r+dr, c+dc
                    if rr not in range(rows) or cc not in range(cols) or grid[rr][cc] == 0:
                        self.res += 1
                    elif rr in range(rows) and cc in range(cols) and grid[rr][cc] == 1 and (rr,cc) not in visit:
                        visit.add((rr,cc))
                        q.append((rr,cc))
            
        rows,cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]:
                    bfs(r,c)
                    return self.res
        return self.res




        
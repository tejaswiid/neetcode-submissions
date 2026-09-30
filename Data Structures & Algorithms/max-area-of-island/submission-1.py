class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        def bfs(i,j):
            res = 1
            q = deque()
            q.append((i,j))
            dirs = [[0,1],[1,0],[-1,0],[0,-1]]
            while q:
                for _ in range(len(q)):
                    r,c = q.popleft()
                    for dr,dc in dirs:
                        rr, cc = r+dr, c+dc
                        if rr in range(rows) and cc in range(cols) and grid[rr][cc] == 1 and (rr,cc) not in visit:
                            res += 1
                            q.append((rr,cc))
                            visit.add((rr,cc))
            return res
        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visit:
                    visit.add((r,c))
                    res = max(res,bfs(r,c))
        return res
                    


        
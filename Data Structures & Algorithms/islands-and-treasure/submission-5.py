class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        INF = 2**31 - 1
        q = deque()
        visit = set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visit.add((r,c))
        dirs = [[0,1],[1,0],[-1,0],[0,-1]]
        res = 1
        while q:
            for _ in range(len(q)):
                r,c = q.popleft()
                for dr,dc in dirs:
                    rr, cc = r+dr, c+dc
                    if rr in range(rows) and cc in range(cols) and grid[rr][cc] == INF and (rr,cc) not in visit:
                        grid[rr][cc] = res
                        visit.add((rr,cc))
                        q.append((rr,cc))
            res += 1
    



        
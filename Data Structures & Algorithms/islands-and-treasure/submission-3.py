class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))
        visit = set()
        time = 0
        while q:
            time += 1
            for i in range(len(q)):
                r,c = q.popleft()
                visit.add((r,c))
                directions = [[0,1],[1,0],[-1,0],[0,-1]]
                for dr, dc in directions:
                    rr, cc = dr+r, dc+c
                    if rr in range(rows) and cc in range(cols):
                        if grid[rr][cc] == 2147483647 and (rr,cc) not in visit:
                            grid[rr][cc] = time
                            visit.add((rr,cc))
                            q.append((rr,cc))
        
        
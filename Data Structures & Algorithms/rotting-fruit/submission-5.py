class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        visit = set()
        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                    visit.add((r,c))
        dirs = [[0,1],[1,0],[0,-1],[-1,0]]
        while q:
            for _ in range(len(q)):
                r,c = q.popleft()
                for dr,dc in dirs:
                    rr, cc = r+dr, c+dc
                    if rr in range(rows) and cc in range(cols) and grid[rr][cc] == 1 and (rr,cc) not in visit:
                        visit.add((rr,cc))
                        q.append((rr,cc))
                        grid[rr][cc] = 2
            res += 1
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1
        return res-1 if res > 0 else res

        
        
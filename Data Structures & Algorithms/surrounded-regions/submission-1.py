class Solution:
    def solve(self, grid: List[List[str]]) -> None:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if r == 0 or c == 0 or r == rows-1 or c == cols-1:
                    if grid[r][c] == "O":
                        q.append((r,c))
                        visit.add((r,c))
        dirs = [[0,1],[1,0],[0,-1],[-1,0]]
        while q:
            r,c = q.popleft()
            for dr,dc in dirs:
                rr,cc = r+dr, c+dc
                if rr in range(rows) and cc in range(cols):
                    if grid[rr][cc] == "O" and (rr,cc) not in visit:
                        q.append((rr,cc))
                        visit.add((rr,cc))
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "O" and (r,c) not in visit:
                    grid[r][c] = "X"



        
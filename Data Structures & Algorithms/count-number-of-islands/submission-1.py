class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit = set()
        rows, cols = len(grid), len(grid[0])
        def bfs(r,c):
            q = deque()
            q.append((r,c))
            while q:
                dirs = [[0,1],[1,0],[-1,0],[0,-1]]
                r,c = q.popleft()
                for dr,dc in dirs:
                    rr, cc = r+dr, c+dc
                    if rr in range(rows) and cc in range(cols) and (rr,cc) not in visit and grid[r][c] == "1":
                        visit.add((rr,cc))
                        q.append((rr,cc))
        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    visit.add((r,c))
                    bfs(r,c)
                    res += 1
        return res


        
                    
                    


        
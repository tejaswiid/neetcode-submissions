class Solution:
    def pacificAtlantic(self, grid: List[List[int]]) -> List[List[int]]:
        pac, atl = [], []
        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if r == 0 or c == 0:
                    pac.append((r,c))
                if r == rows-1 or c == cols-1:
                    atl.append((r,c))
        def bfs(q,visit):
            q = deque(q)
            visit = set(visit)
            while q:
                for _ in range(len(q)):
                    r,c = q.popleft()
                    dirs = [[0,1],[0,-1],[-1,0],[1,0]]
                    for dr,dc in dirs:
                        rr, cc = r+dr, c+dc
                        if rr in range(rows) and cc in range(cols):
                            if grid[rr][cc] >= grid[r][c] and (rr,cc) not in visit:
                                q.append((rr,cc))
                                visit.add((rr,cc))
            return visit
        pac = bfs(pac,pac)
        atl = bfs(atl,atl)
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        return res

        
            


        
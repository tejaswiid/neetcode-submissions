class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visit = set()
        rows, cols = len(grid), len(grid[0])
        def bfs(r,c):
            q = deque()
            q.append((r,c))
            area = 1
            while q:
                # print(q)
                dirs = [[0,1],[1,0],[-1,0],[0,-1]]
                r,c = q.popleft()
                for dr,dc in dirs:
                    rr, cc = r+dr, c+dc
                    if rr in range(rows) and cc in range(cols) and (rr,cc) not in visit and grid[rr][cc] == 1:
                        
                        visit.add((rr,cc))
                        q.append((rr,cc))
                        area += 1
            # print(area)
            return area
        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visit:
                    visit.add((r,c))
                    res = max(res,bfs(r,c))
        return res


        
                    
                    


        
        
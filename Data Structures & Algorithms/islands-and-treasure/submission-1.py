class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        q = deque()
        def addnum(r,c):
            if r not in range(rows) or c not in range(cols) or grid[r][c] == -1 or (r,c)  in visit:
                return 
            q.append((r,c))
            visit.add((r,c))
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    visit.add((r,c))
                    q.append((r,c))
        time = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = time
                addnum(r+1,c)
                addnum(r,c+1)
                addnum(r-1,c)
                addnum(r,c-1)
            time += 1
        


                
            
        
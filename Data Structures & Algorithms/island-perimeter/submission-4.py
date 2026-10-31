class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dirs = [[0,1],[1,0],[0,-1],[-1,0]]
        visit = set()
        def bfs(r,c):
            perimeter = 0
            q = deque()
            q.append((r,c))
            visit.add((r,c))
            while q :
            
                r,c = q.popleft()
                for dr, dc in dirs:
                    rr , cc = r+dr, c+dc
                    if rr not in range(rows) or cc not in range(cols) or grid[rr][cc] == 0:
                        perimeter += 1
                    elif (rr,cc) not in visit:
                        q.append((rr,cc))
                        visit.add((rr,cc))
                        
            return perimeter
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]:
                    return bfs(r,c)
        return 0
                            


        
        
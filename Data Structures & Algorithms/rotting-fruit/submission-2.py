class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()

        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
    
        time = 0
        dirs = [[0,1],[1,0],[-1,0],[0,-1]]
        while q:
            isit = 0
            for _ in range(len(q)):
                r,c = q.popleft()
                for dr,dc in dirs:
                    rr, cc = r+dr, c+dc
                    if rr in range(rows) and cc in range(cols):
                        if grid[rr][cc] == 1:
                            grid[rr][cc] = 2
                            isit += 1
                            q.append((rr,cc))
            if isit : time += 1
        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1 
        return time
        


        
        
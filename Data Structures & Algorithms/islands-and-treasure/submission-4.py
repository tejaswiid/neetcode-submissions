class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        dirs = [[0,1],[1,0],[-1,0],[0,-1]]
            
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))
        steps = 0
        while q:
            for _ in range(len(q)):
                r,c = q.popleft()
                for dr,dc in dirs:
                    rr , cc = r+dr, c+dc
                    if 0 <= rr <= rows-1 and 0 <= cc <= cols-1:
                        if grid[rr][cc] == 2147483647:
                            grid[rr][cc] = steps + 1
                            q.append((rr,cc))
            steps += 1
        
                    

                



        
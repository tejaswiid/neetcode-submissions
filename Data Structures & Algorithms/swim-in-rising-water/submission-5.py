class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
     
        rows, cols = len(grid), len(grid[0])
        dirs = [[0,1],[1,0],[-1,0],[0,-1]]
        q = []
        heapq.heappush(q,[grid[0][0],0,0])
        visit = set()
        visit.add((0,0))
        res = float("inf")
        while q:
            t,r,c = heapq.heappop(q)
            if r == rows-1 and c == cols-1:
                return t 
            for dr,dc in dirs:
                rr, cc = r+dr, c+dc
                if rr in range(rows) and cc in range(cols) and (rr,cc) not in visit:
                    visit.add((rr,cc))
                    heapq.heappush(q,(max(grid[rr][cc],t),rr,cc))
        


        
class Solution:
    def minimumEffortPath(self, grid: List[List[int]]) -> int:
        heap = []
        rows,cols = len(grid), len(grid[0])
        heapq.heappush(heap,[0,0,0])
        dirs = [[0,-1],[0,1],[1,0],[-1,0]]
        visit = set()
        # visit.add((0,0))
        res = float("inf")
        while heap:
            val,r,c = heapq.heappop(heap)
            if (r,c) in visit: 
                continue
            visit.add((r,c))
            if r == rows-1 and c == cols-1:
                return val
    
            for dr,dc in dirs:
                rr, cc = r+dr, c+dc
                if rr in range(rows) and cc in range(cols) and (rr,cc) not in visit:

                    new_val = max(val,abs(grid[r][c]-grid[rr][cc]))
                    heapq.heappush(heap,[new_val,rr,cc])
      
            


        
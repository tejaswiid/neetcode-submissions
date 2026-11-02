class Solution:
    def minimumEffortPath(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        heap = []
        heapq.heappush(heap,(0,0,0))
        dirs = [[0,1],[1,0],[-1,0],[0,-1]]
        visit = set()
        
        while heap:
            res,r,c = heapq.heappop(heap)
            if r == rows-1 and c == cols-1:
                return res
            if (r,c) in visit:
                continue
            visit.add((r,c))
            for dr,dc in dirs:
                rr, cc = r+dr, c+dc
                if rr in range(rows) and cc in range(cols):
                    if (rr,cc) not in visit:
                        val = max(res,abs(grid[r][c] - grid[rr][cc]))
                        heapq.heappush(heap,(val,rr,cc))
            
           
        



        
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        heap = [[grid[0][0],0,0]]
        visit = set()
        visit.add((0,0))
        while heap:
            t,r,c = heapq.heappop(heap)
            if r == rows-1 and c == cols-1:
                return t
            dirs = [[0,1],[1,0],[-1,0],[0,-1]]
            for dr,dc in dirs:
                rr, cc = r+dr, c+dc
                if rr in range(rows) and cc in range(cols):
                    if (rr,cc) not in visit:
                        heapq.heappush(heap,[max(grid[rr][cc],t),rr,cc])
                        visit.add((rr,cc))
        
        
        
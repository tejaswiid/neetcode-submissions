class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        res = float("inf")
        heap = [[grid[0][0],0,0]]
        visit = set()
        dirs = [[0,1],[1,0],[-1,0],[0,-1]]
        while heap:
            val,r,c = heapq.heappop(heap)
            # print(val,r,c)
            if (r,c) in visit:
                continue
            visit.add((r,c))
            if r == rows-1 and c == cols-1:
                return val
            for dr,dc in dirs:
                rr,cc = r+dr, c+dc
                if rr in range(rows) and cc in range(cols):
                    if (rr,cc) not in visit:
                        heapq.heappush(heap,[max(val,grid[rr][cc]),rr,cc])

            

        
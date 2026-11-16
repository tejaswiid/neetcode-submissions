class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        heap = [[grid[0][0],0,0]]
        dirs = [[0,1],[1,0]]
        visit = set()
        while heap:
            dist,r,c = heapq.heappop(heap)
            if r == rows-1 and c == cols-1: 
                return dist
            if (r,c) in visit: continue
            visit.add((r,c))
            for dr,dc in dirs:
                rr,cc = r+dr,c+dc
                if rr in range(rows) and cc in range(cols):
                    if (rr,cc) not in visit:
                        heapq.heappush(heap,[dist+grid[rr][cc],rr,cc])
        
                

            


        
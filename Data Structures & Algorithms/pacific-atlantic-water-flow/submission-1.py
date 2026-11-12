class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac = set()
        atl = set()
        rows, cols = len(heights), len(heights[0])
        for r in range(rows):
            for c in range(cols):
                if r == 0 or c == 0:
                    pac.add((r,c))
                if r == rows - 1 or c == cols -1:
                    atl.add((r,c))
        dirs = [[0,1],[1,0],[0,-1],[-1,0]]
        def bfs(visit):
            q = deque(list(visit))
            while q:
                for _ in range(len(q)):
                    r,c = q.popleft()
                    for dr,dc in dirs:
                        rr,cc = r+dr, c+dc
                        if rr in range(rows) and cc in range(cols) and heights[rr][cc] >= heights[r][c] and (rr,cc) not in visit:
                            visit.add((rr,cc))
                            q.append((rr,cc))
            return visit
        pac = bfs(pac)
        atl = bfs(atl)
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        return res
                

        
        
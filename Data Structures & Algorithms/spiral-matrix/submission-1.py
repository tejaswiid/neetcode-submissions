class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])
        dirs = {"r": [0,1], "l":[0,-1],"u":[-1,0],"d":[1,0]}
        nxt = {"r":"d","d":"l","l":"u","u":"r"}
        res = []
        visit = set()
        def dfs(r,c,v):
            if len(visit) == rows*cols: return 
            if (r,c) not in visit:
                res.append(matrix[r][c])
            visit.add((r,c))
            dr,dc = dirs[v]
            rr, cc = r+dr, c+dc
            if (rr) not in range(rows) or cc not in range(cols) or (rr,cc) in visit:
                dfs(r,c,nxt[v])

            elif rr in range(rows) and cc in range(cols) and(rr,cc) not in visit:
                dfs(rr,cc,v)
            return 
        dfs(0,0,"r")
        return res

                
        
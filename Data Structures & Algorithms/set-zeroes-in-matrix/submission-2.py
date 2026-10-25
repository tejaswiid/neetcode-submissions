class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n, m = len(matrix) , len(matrix[0])
        cols = []
        rows = []
        for r in range(n):
            for c in range(m):
                if matrix[r][c] == 0:
                    cols.append(c)
                    rows.append(r)
        for c in range(m):
            if c in cols:
                for r in range(n):
                    matrix[r][c] = 0
        for r in range(n):
            if r in rows:
                for c in range(m):
                    matrix[r][c] = 0
        
        
        
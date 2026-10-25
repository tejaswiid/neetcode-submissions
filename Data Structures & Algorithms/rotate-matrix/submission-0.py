class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        new_matrix = [[0 for _ in range(n)] for _ in range(n)]
        i = 0
        while i < n:
            for c in range(n-1,-1,-1):
                m = matrix[i]
                for r in range(n):
                    new_matrix[r][c] = m[r]
                i += 1
    
        for r in range(n):
            for c in range(n):
                matrix[r][c] = new_matrix[r][c]



            

        
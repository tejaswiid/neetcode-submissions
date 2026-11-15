class Solution:
    def totalNQueens(self, n: int) -> int:
        board = [["." for _ in range(n)] for _ in range(n)]
        self.res = 0
        def bactrack(i):
            if i == n:
                self.res += 1
                return 
            for j in range(n):
                if issafe(i,j,board):
                    board[i][j] = "Q"
                    bactrack(i+1)
                    board[i][j] = "."
       
        def issafe(r,c,board):
            for i in range(n):
                if board[r][i] == "Q":
                    return False
            for i in range(n):
                if board[i][c] == "Q":
                    return False
            i, j = r-1, c-1
            while i >= 0 and j >= 0:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j -= 1

            # Check upper-right diagonal
            i, j = r-1, c+1
            while i >= 0 and j < n:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j += 1

            return True
        bactrack(0)
        return self.res
                

        
        
        
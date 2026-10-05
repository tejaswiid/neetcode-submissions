class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["." for _ in range(n)] for _ in range(n)]
        def backtrack(r):
            if r == n :
                copy = ["".join(row) for row in board]
                res.append(copy)
                return 
            

            for i in range(n):
                if issafe(r,i,board):
                    board[r][i] = "Q"
                    backtrack(r+1)
                    board[r][i] = "."
      
        def issafe(r,c,board):
            rows = r - 1
            while rows >= 0:
                if board[rows][c] == "Q":
                    return False
                rows -= 1
            rows , cols = r - 1, c - 1
            while rows >= 0 and cols >= 0:
                if board[rows][cols] == "Q":
                    return False
                rows -= 1
                cols -= 1
            rows , cols = r-1, c+1
            while rows >= 0 and cols < len(board):
                if board[rows][cols] == "Q":
                    return False
                rows -= 1
                cols += 1
            return True
        backtrack(0)
        return res

        
        
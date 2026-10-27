class Solution:
    def totalNQueens(self, n: int) -> int:
        res = []
        board = [["." for _ in range(n)] for _ in range(n)]
        def backtrack(r):
            if r == n:
                val = ["".join(row) for row in board]
                res.append(val)
                return 
            for c in range(n):
                if issafe(r,c,board):
                    board[r][c] = "Q"
                    backtrack(r+1)
                    board[r][c] = "."

        def issafe(r,c,board):
            for i in range(r-1,-1,-1):
                if board[i][c] == "Q":
                    return False
            rows, cols = r - 1, c - 1
            while rows >= 0 and cols >= 0:
                if board[rows][cols] == "Q":
                    return False
                rows -= 1
                cols -= 1
            rows, cols = r - 1, c + 1
            while rows >= 0 and cols < n:
                if board[rows][cols] == "Q":
                    return False
                rows -= 1
                cols += 1
            return True
        backtrack(0)
        # print(res)
  
        return len(res)

        

        
        
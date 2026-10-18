class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isvalid(i,j):
            num = board[i][j]
            for r in range(9):
                if r != i and board[r][j] == num:
                    print(r,j)
                    return False
            for c in range(9):
                if c != j and board[i][c] == num:
                    print(i,c)
                    return False
            def grid(u,v):
                for r in range(v,v+3):
                    for c in range(u,u+3):
                        if r != i and c != j and board[r][c] == num:
                            return False
                return grid
            if i < 3: v = 0
            elif i >= 3 and i < 6: v = 3
            else: v = 6
            if j < 3: u = 0
            elif j >= 3 and j < 6: u = 3
            else: u = 6
            if not grid(u,v): return False
            
            return True

            
            
    
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    if not isvalid(i,j):
                        print(i,j,board[i][j])
                        return False
        return True

        
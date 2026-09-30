class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        q = deque()
        visit = set()
        for r in range(rows):
            for c in range(cols):
                if r == 0 or c == 0 or r == rows-1 or c == cols-1:
                    if board[r][c] == "O":
                        q.append((r,c))
                        visit.add((r,c))
        while q:
            for _ in range(len(q)):
                r,c = q.popleft()
                dirs = [[0,1],[0,-1],[1,0],[-1,0]]
                for dr,dc in dirs:
                    rr, cc = r+dr, c+dc
                    if rr in range(rows) and cc in range(cols):
                        if board[rr][cc] == "O" and (rr,cc) not in visit:
                            q.append((rr,cc))
                            visit.add((rr,cc))
            
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r,c) not in visit:
                    board[r][c] = "X"


        

        
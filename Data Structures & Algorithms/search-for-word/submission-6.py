class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        
        def dfs(i,j,word):
            # print(i,j,word)
            if len(word) == 0:
                return True
            dirs = [[0,1],[1,0],[0,-1],[-1,0]]
            first = word[0]
            word = word[1:]
            
            # print(first,word)
            for dr,dc in dirs:
                rr, cc = i+dr, j+dc
                if rr in range(rows) and cc in range(cols) and (rr,cc) not in visit:
                    if board[rr][cc] == first:
                        visit.add((rr,cc))
                        # print(board[rr][cc])
                        if dfs(rr,cc,word):
                            return True
                        visit.remove((rr,cc))
            return False
      
        first = word[0]
        word = word[1:]
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == first:
                    visit = set()
                    visit.add((r,c))
                    if dfs(r,c,word):
                        return True
        return False
       
#  A B C E
#  S F E S
#  A D E E


                    
        
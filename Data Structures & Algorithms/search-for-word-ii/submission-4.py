class TrieNode:
    def __init__(self):
        self.children = {}
        self.endofword = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        def addword(word,node):
            for w in word:
                if w not in node.children:
                    node.children[w] = TrieNode()
                node = node.children[w]
            node.endofword = True
        for word in words:
            addword(word,root)
        rows, cols = len(board), len(board[0])
        res = set()
        neis = [[0,1],[1,0],[0,-1],[-1,0]]
        def dfs(node,r,c,ans):
            val = board[r][c]
            if val not in node.children:
                return 
            visit.add((r,c))
            node = node.children[val]
            ans += val
            if node.endofword:
                res.add(ans)
            for dr,dc in neis:
                rr, cc = r+dr, c+dc
                if rr in range(rows) and cc in range(cols) and (rr,cc) not in visit:
                    dfs(node,rr,cc,ans)
            visit.remove((r,c))
        for r in range(rows):
            for c in range(cols):
                visit = set()
                dfs(root,r,c,"")
        return list(res)



        
        
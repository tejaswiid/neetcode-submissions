class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {}
        for word in words:
            for c in word:
                adj[c] = set()
        def connect(word1,word2):
            i,j = 0, 0 
            for i in range(len(word1)):
                if i >= len(word2): return False
                if word1[i] != word2[i]:
                    adj[word1[i]].add(word2[i])
                    return True
                    break
            return True
        for i in range(1,len(words)):
            val = connect(words[i-1],words[i])
            if not val: return ""
        res = []
        visit = {}
        def dfs(node):
            if node in visit: return visit[node]
            visit[node] = True
            for nei in adj[node]:
                if dfs(nei): return ""
            visit[node] = False
            res.append(node)
        for c in adj:
            if dfs(c): return ""
        return "".join(res[::-1])
                


        

        
        
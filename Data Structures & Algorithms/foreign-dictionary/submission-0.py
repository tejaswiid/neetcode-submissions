class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {}
        for w in words:
            for c in w:
                adj[c] = set()
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            minl = min(len(w1),len(w2))
            if len(w1) > len(w2) and w1[:minl] == w2[:minl]:
                return ""
            for j in range(minl):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        res = []
        visit = {}
        def dfs(n):
            if n in visit: return visit[n]
            visit[n] = True
            for nei in adj[n]:
                if dfs(nei):
                    return True
            visit[n] = False
            res.append(n)
        for c in adj:
            if dfs(c): return ""
        res = res[::-1]
        return "".join(res)

            


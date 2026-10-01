class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for e1,e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)
        visit = set()
        res = 0
        def dfs(i):
            if i in visit:
                return 
            visit.add(i)
            for nei in adj[i]:
                dfs(nei)
            return 
        for i in range(n):
            if i not in visit:
                dfs(i)
                res += 1
        return res
            



        
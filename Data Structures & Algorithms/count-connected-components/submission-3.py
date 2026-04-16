class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adj = defaultdict(list)
        for e1,e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)

        visit = set()
        def dfs(node):
            if node in visit:
                return 
            visit.add(node)
            for nei in adj[node]:
                dfs(nei)
            return 
        res = 0
        for i in range(n):
            if i not in visit:
                res += 1
                dfs(i)
                print(visit)
        return res
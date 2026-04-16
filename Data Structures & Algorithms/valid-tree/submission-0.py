class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for e1,e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)
        cycle = set()
        def dfs(n,par):
            if n in cycle:
                return False
            cycle.add(n)
            for nei in adj[n]:
                if nei == par: continue
                if not dfs(nei,n): return False
            return True
        return dfs(0,-1) and len(cycle) == n
       








        
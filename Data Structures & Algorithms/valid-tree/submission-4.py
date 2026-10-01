class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for e1,e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)
        visit = set()
        def dfs(i,root):
            if i in visit: return False
            visit.add(i)
            for nei in adj[i]:
                if nei != root:
                    if not dfs(nei,i):
                        return False
            
            return True
        if not dfs(0,-1):
            return False
        return len(visit) == n
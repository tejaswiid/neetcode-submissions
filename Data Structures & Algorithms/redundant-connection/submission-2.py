class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def dfs(node,par):
            if node in visit:
                return True
            visit.add(node)
            for nei in adj[node]:
                if nei == par:
                    continue
                if dfs(nei,node):
                    return True
            return False
        u,v = 0,0
        adj = defaultdict(list)
        for e1,e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)
            visit = set()
            if dfs(e1,e2):
                u,v = e1,e2
                return [u,v]
       
                
        
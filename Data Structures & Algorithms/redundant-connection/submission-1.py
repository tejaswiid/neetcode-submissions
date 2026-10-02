class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def dfs(node,par):
            if visit[node]:
                return True
            visit[node] = True
            for nei in adj[node]:
                if nei == par:
                    continue
                if dfs(nei,node):
                    return True
            return False
        adj = defaultdict(list)
        for e1,e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)
            visit = [False] * (len(edges)+1)
            if dfs(e1,-1):
                return [e1,e2]
        return []

        
        
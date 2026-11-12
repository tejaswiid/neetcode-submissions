class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        seen = set()
        adj = defaultdict(list)
        for e1,e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)
        def dfs(node,par,cycle):
            if node in cycle:
                return False
            if node in seen: return True
            cycle.add(node)
            for nei in adj[node]:
                if nei != par and nei != node:
                    if not dfs(nei,node,cycle):
                        return False
            cycle.remove(node)
            seen.add(node)
            return True
    

        if not dfs(0,-1,set()): return False
    
        return len(seen) == n


        
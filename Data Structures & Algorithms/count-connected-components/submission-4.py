class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = list(range(n))
        def find(i):
            if i != par[i]:
                par[i] = find(par[i])
            return par[i]
        def union(a,b):
            par[find(a)] = find(b)
        
        for a,b in edges:
            union(a,b)
        root = set()
        for i in range(n):
            root.add(find(i))
        return len(root)
        
        
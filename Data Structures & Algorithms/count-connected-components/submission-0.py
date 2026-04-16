class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n+1)]
        rank = [1]*(n+1)
        def find(n):
            p = par[n]
            if p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p
        def union(n1,n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                rank[p1] += rank[p2]
                par[p2] = p1
            else:
                rank[p2] += rank[p1]
                par[p1] = p2
            return True
        count = n
        for n1,n2 in edges:
            if union(n1,n2):
                count -= 1
        return count
            
        
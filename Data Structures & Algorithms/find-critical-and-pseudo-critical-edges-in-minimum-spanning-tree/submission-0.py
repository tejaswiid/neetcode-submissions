class UnionFind:
    def __init__(self,n):
        self.rank = [1]*n
        self.par = [i for i in range(n)]
    def find(self,n1):
        while n1 != self.par[n1]:
            self.par[n1] = self.par[self.par[n1]]
            n1 = self.par[n1]
        return n1
    def union(self,n1,n2):
        p1,p2 = self.find(n1),self.find(n2)
        if p1 == p2: return 0
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        return 1
class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        for i, e in enumerate(edges):
            e.append(i)
        edges.sort(key = lambda e: e[2])
        mst_weight = 0
        uf = UnionFind(n)
        for e1,e2,w,i in edges:
            if uf.union(e1,e2):
                mst_weight += w
        critical, psuedo = [], []
        for n1,n2,e_weight,i in edges:
            weight = 0
            uf = UnionFind(n)
            for e1,e2,w,j in edges:
                if i != j and uf.union(e1,e2):
                    weight += w
            if max(uf.rank) != n or weight > mst_weight :
                critical.append(i)
                continue
            weight = e_weight
            uf = UnionFind(n)
            uf.union(n1,n2)
            for e1,e2,w,j in edges:
                if uf.union(e1,e2):
                    weight += w
            if weight == mst_weight:
                psuedo.append(i)
        return [critical,psuedo]

            

        
        
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
        for i in range(len(values)):
            e1,e2 = equations[i]
            v = values[i]
            adj[e1].append((e2,v))
            adj[e2].append((e1,1/v))
        def dfs(node,des):
            if node == des:
                return 1
            if node in visit:
                return -1
            visit.add(node)
           
            for nei,p in adj[node]:
                if nei not in visit:
                    v = dfs(nei,des)
                    if v != -1:
                        # v *= p
                        return p*v
                    # val /= p
            return -1
        res = []
        for q1,q2 in queries:
            visit = set()
            if q1 in adj and q2 in adj:
                res.append(dfs(q1,q2))
            else: res.append(-1)
        return res
        



        
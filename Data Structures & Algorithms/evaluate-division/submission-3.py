class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
        for i,e in enumerate(equations):
            e1,e2 = e
            adj[e1].append([e2,values[i]])
            adj[e2].append([e1,1/values[i]])
        
        def dfs(node,dst,val):
            if node == dst:
                return val
            if node in visit: return -1
            visit.add(node)
            for nei,v in adj[node]:
                if nei not in visit:
                    val *= v
                    res = dfs(nei,dst,val)
                    if res != -1:
                        return res
                    val /= v
            return -1
        res = []
        for q1,q2 in queries:
            visit = set()
            if q1 in adj and q2 in adj:
                res.append(dfs(q1,q2,1))
            else: res.append(-1)
        return res

            

        
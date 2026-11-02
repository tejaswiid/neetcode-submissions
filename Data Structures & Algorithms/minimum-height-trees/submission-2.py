class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1: return [0]
        adj = defaultdict(list)
        degree = [0]*n
        for e1,e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)
            degree[e1] += 1
            degree[e2] += 1
        res = defaultdict(list)
        def height(node):
            q = deque()
            q.append(node)
            visit.add(node)
            h = 0
            while q:
                for _ in range(len(q)):
                    node = q.popleft()
                    for nei in adj[node]:
                        if nei not in visit:
                            visit.add(nei)
                            q.append(nei)
                h += 1
            return h
        minh = float("inf")
        for i in range(n):
        
            visit = set()
            h = height(i)
            res[h].append(i)
            minh = min(minh,h)
        return res[minh]
       
        


        
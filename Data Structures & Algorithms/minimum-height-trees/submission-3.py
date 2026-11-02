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
        q = deque()
        for i in range(n):
            if degree[i] == 1:
                q.append(i)
        while n > 2:
            n -= len(q)
            for _ in range(len(q)):
                node = q.popleft()
                for nei in adj[node]:
                    degree[nei] -= 1
                    if degree[nei] == 1:
                        q.append(nei)
        return list(q)

       
        


        
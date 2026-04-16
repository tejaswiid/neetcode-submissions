class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for e1,e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)
        q = deque()
        q.append((0,-1))
        visit = set()
        while q:
            for _ in range(len(q)):
                node,par = q.popleft()
                if node in visit: return False
                visit.add(node)
                for nei in adj[node]:
                    if nei == par:
                        continue
                    q.append((nei,node))
        return len(visit) == n

                

        
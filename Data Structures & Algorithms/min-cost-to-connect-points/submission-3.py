class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = defaultdict(list)
        for i in range(n):
            x1,y1 = points[i][0], points[i][1]
            for j in range(i+1,n):
                x2,y2 = points[j][0], points[j][1]
                dist = abs(x1-x2) + abs(y1-y2)
                adj[i].append([dist,j])
                adj[j].append([dist,i])
        heap = [[0,0]]
        visit = set()
        res = 0
        while heap:
            cost, node = heapq.heappop(heap)
            if node in visit: continue
            visit.add(node)
            res += cost
            if len(visit) == n:
                return res
            for c, nei in adj[node]:
                heapq.heappush(heap,[c,nei])



       

        
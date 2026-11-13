class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = defaultdict(list)
        for i,p in enumerate(points):
            x1,y1 = p
            for j,p2 in enumerate(points):
                if i != j:
                    x2,y2 = p2
                    dis = abs(x1-x2) + abs(y1-y2)
                    adj[i].append([dis,j])
        visit = set()
        res = 0
        heap = [[0,0]]
        while heap:
            dis,node = heapq.heappop(heap)
            if node in visit:
                continue
            visit.add(node)
            res += dis
            if len(visit) == len(points): return res
            for n_dis,new_node in adj[node]:
                heapq.heappush(heap,[n_dis,new_node])

        
            


        
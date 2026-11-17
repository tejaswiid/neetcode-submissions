class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for f1,f2,c in flights:
            adj[f1].append([f2,c])
        heap = [[0,0,src]]
        dist = {}
        dist[(src,0)] = 0
        while heap:
            dis, stops, node = heapq.heappop(heap)
            if node == dst: return dis
            if stops == k+1 or dis > dist[(node,stops)]:
                continue
            for nei,cost in adj[node]:
                new = dis + cost
                if new < dist.get((nei,stops+1),float("inf")):
                    dist[(nei,stops+1)] = new
                    heapq.heappush(heap,[new,stops+1,nei])
        return -1
        
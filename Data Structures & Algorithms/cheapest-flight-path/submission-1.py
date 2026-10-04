class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for f,t,price in flights:
            adj[f].append([t,price])
        heap = [[0,src,0]]
        dist = {}
        dist[(src,0)] = 0 
        while heap:
            dis, node, stops = heapq.heappop(heap)
            if node == dst:
                return dis
            if stops == k+1 or dis > dist[(node,stops)]:
                continue
            for nei, price in adj[node]:
                new = price + dis
                if new < dist.get((nei,stops+1),float("inf")):
                    dist[(nei,stops+1)] = new
                    heapq.heappush(heap,[new,nei,stops+1])


        return -1
            
        
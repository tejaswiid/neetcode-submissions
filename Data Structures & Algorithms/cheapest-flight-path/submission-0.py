class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for f,t,price in flights:
            adj[t].append([f,price])
        heap = [[0,dst,0]]
        while heap:
            dis, node, stops = heapq.heappop(heap)
            if node == src and stops <= k:
                return dis
            for nei, price in adj[node]:
                if nei != src and stops + 1 <= k :
                    heapq.heappush(heap,[price+dis,nei,stops+1])
                if nei == src:
                    heapq.heappush(heap,[price+dis,nei,stops])

        return -1
            
        
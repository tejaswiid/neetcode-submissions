class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u,v,t in times:
            adj[u].append((v,t))
        heap = [(0,k)]
        visit = set()
        while heap:
            time, node = heapq.heappop(heap)
            # print(node)
            if node in visit:
                continue
            visit.add(node)
            if len(visit) == n:
                return time
            for nei,t in adj[node]:
                # print(nei)
                if nei not in visit:
                    heapq.heappush(heap,(t+time,nei))
        return -1
    

        
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u,v,t in times:
            adj[u].append((v,t))
        visit = set()
        heap = [[0,k]]
        while heap:
            time, node = heapq.heappop(heap)
            if node in visit: continue
            visit.add(node)
            if len(visit) == n:
                return time
            for nei,t in adj[node]:
                if nei not in visit:
                    heapq.heappush(heap,[time+t,nei])
        return -1

        
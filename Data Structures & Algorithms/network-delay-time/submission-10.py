class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        heap = [[0,k]]
        adj = defaultdict(list)
        for n1,n2,t in times:
            adj[n1].append([n2,t])
        min_time, nodes = float("inf"), 0
        visit = set()
        while heap:
            time,node = heapq.heappop(heap)
            if node in visit: continue
            visit.add(node)
            nodes += 1
            if nodes == n:
                return time
            for nei,t in adj[node]:
                heapq.heappush(heap,[time+t,nei])
        return -1

        
            
        
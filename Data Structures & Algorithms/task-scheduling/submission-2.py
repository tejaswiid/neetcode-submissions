class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = []
        q = deque()
        dic = Counter(tasks)
        for k,v in dic.items():
            heapq.heappush(heap,-v)
        time = 0
        while q or heap:
            time += 1
            if heap:
                val = heapq.heappop(heap)
                if val+1 < 0:q.append((val+1,time+n))
            if q and q[0][1] == time:
                val,k = q.popleft()
                heapq.heappush(heap,val)
        return time


        
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        dic = Counter(tasks)
        heap = []
        for k,v in dic.items():
            heapq.heappush(heap,-v)
        time = 0
        q = deque()
        while heap or q:
            time += 1
            if heap:
                cnt = 1 + heapq.heappop(heap)
                if cnt:
                    q.append([cnt,time+n])
            if q and q[0][1] == time:
                heapq.heappush(heap,q.popleft()[0])
        return time
            







        
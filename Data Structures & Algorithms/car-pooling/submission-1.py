class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        heap = []
        for t1,t2,t3 in trips:
            heapq.heappush(heap,[t2,t3,t1])
        dist = 1
        cur = 0
        new_heap = []
        while heap:
            dist = heap[0][0]
            while new_heap and new_heap[0][0] <= dist:
                _,c = heapq.heappop(new_heap)
                cur -= c
            while heap and heap[0][0] == dist:
                st,end,cap = heapq.heappop(heap)
                cur += cap
                heapq.heappush(new_heap,[end,cap])
                if cur > capacity: return False
            
        return True
        






        
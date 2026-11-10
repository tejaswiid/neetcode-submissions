class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        heap = []
        for i,t in enumerate(tasks):
            val = t + [i]
            heapq.heappush(heap,val)
        res = []
        time = 0 

        while heap:
            heap2 = []
            while heap and heap[0][0] <= time:
                t1,t2,ind = heapq.heappop(heap)
                heapq.heappush(heap2,(t2,ind))
            if not heap2:
                time += 1
                continue
            print(heap,heap2)
            while heap2:
                # print(heap,heap2,time)
                t2,ind = heapq.heappop(heap2)
                time += t2
                res.append(ind)
                while heap and heap[0][0] <= time:
                    t1,t2,ind = heapq.heappop(heap)
                    heapq.heappush(heap2,(t2,ind))
                
            
        return res
        # 2,1,3

            
        
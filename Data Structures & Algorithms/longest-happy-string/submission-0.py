class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = ""
        heap = []
        if a: heapq.heappush(heap,[-a,"a"]) 
        if b: heapq.heappush(heap,[-b,"b"])
        if c: heapq.heappush(heap,[-c,"c"])
        prev1,prev2 = None, None
        while heap:
            new_heap = []
            while heap and prev1 == prev2 == heap[0][1]:
                num,val = heapq.heappop(heap)
                heapq.heappush(new_heap,[num,val])
            if not heap:
                return res
            num,val = heapq.heappop(heap)
            res += val
            if num+1:
                heapq.heappush(heap,[num+1,val])
            prev1,prev2 = val,prev1
            while new_heap:
                num,val = heapq.heappop(new_heap)
                heapq.heappush(heap,[num,val])
        return res

                


        
class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        heap = [[-v,cnt] for cnt,v in count.items()]
        heapq.heapify(heap) 
        prev = None
        res = ""
        while heap or prev:
            if prev and not heap: return ""
            cnt, v = heapq.heappop(heap)
            res += v
            if prev:
                heapq.heappush(heap,prev)
                prev = None
            if cnt + 1:
                prev = [cnt+1,v]
        return res
            

        
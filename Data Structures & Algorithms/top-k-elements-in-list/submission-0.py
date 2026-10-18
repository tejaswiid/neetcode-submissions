class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = []
        for key,v in count.items():
            heapq.heappush(heap,(v,key))
        while len(heap) > k:
            heapq.heappop(heap)
        res = [val for _,val in heap]
        return res

        


        
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        count = defaultdict(list)
        for a in arr:
            count[abs(x-a)].append(a)
        count1 = sorted(count)
        res = []
        print(count,count1)
        for c in count1:
            res.extend(count[c])
            if len(res) >= k:
                break
        res = res[:k]
        res.sort()
        return res


        
        
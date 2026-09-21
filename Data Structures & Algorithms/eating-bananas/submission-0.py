class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = max(piles)
        def caneat(r):
            s = 0
            for p in piles:
                s += math.ceil(p/r)
            if s <= h: return True
            return False

        while l <= r:
            m = (l+r) // 2
            if  caneat(m):
                r = m - 1
                res = min(res,m)
            else:
                l = m + 1
        return res

        
        
        
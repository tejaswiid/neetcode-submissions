class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def isit(w):
            i, res = 0, 1
            cur = 0
            while i < len(weights):
                cur += weights[i]
                if cur > w:
                    res += 1
                    cur = weights[i]
                i += 1
            print(res,w)
            return res <= days 

        l , r= max(weights), sum(weights)
        res = r
        while l <= r:
            m = (l+r) // 2
            if isit(m):
                res = min(res,m)
                r = m - 1
            else:
                l = m + 1
        return res

        # 5 - 19 

            

       



        
        


        
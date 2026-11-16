class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        dp = {}
        def dfs(alice,i,m):
            if i == len(piles): return 0
            if (alice,i,m) in dp: return dp[(alice,i,m)]
            res = float("-inf") if alice else float("inf")
            total = 0
            for x in range(2*m):
                if i+x < len(piles):
                    total += piles[i+x]
                    if alice:
                        val = total + dfs(not alice,i+x+1,max(m,x+1))
                        res = max(res,val)
                    else:
                        val = dfs(not alice,i+x+1,max(m,x+1))
                        res = min(res,val)
            dp[(alice,i,m)] = res
            return res
        return dfs(True,0,1)
                


        
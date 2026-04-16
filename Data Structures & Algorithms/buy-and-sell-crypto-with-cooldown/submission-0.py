class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        def dfs(i,buy):
            if i >= len(prices):
                return 0
            if (i,buy) in dp: return dp[(i,buy)]
            if buy:
                dp[(i,buy)] = max(dfs(i+1,0)-prices[i], dfs(i+1,1))
            else:
                dp[(i,buy)] = max(dfs(i+2,1)+prices[i], dfs(i+1,0))
            return dp[(i,buy)]
        return dfs(0,1)
            

            


        
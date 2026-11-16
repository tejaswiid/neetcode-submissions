class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        def dfs(i,buy):
            if i >= len(prices): 
                return 0 
            if (i,buy) in dp: return dp[(i,buy)]
            if buy:
                val = -prices[i] + dfs(i+1,not buy)
                val2 = dfs(i+1,buy)
                
            else:
                val = prices[i] + dfs(i+2,not buy)
                val2 = dfs(i+1,buy)
            res = max(val,val2)
            dp[(i,buy)] = res
            return res
        return dfs(0,True)



        
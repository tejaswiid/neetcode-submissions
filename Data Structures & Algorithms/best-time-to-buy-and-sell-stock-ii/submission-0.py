class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {} 
        def dfs(buy,i):
            if i == len(prices):
                dp[(buy,i)] = 0
                return 0
            val = 0
            if (buy,i) in dp: return dp[(buy,i)]
            if buy:
                val = max(prices[i] + dfs(not buy,i+1), dfs(buy,i+1))
            else:
                val = max(-prices[i]+dfs(not buy,i+1), dfs(buy,i+1))
            dp[(buy,i)] = val
            return val
        return dfs(False,0)


        # 7 - dfs(), 1 







        
   
        
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[-1 for _ in range(len(coins)+1)] for _ in range(amount+1)]
        def dfs(total,i):
            if total > amount or i == len(coins):
                return 0
            if total == amount:
                return 1 
            if dp[total][i] != -1: return dp[total][i]
            val = dfs(total+coins[i],i)
            val += dfs(total,i+1)
            dp[total][i] = val
            return val
        return dfs(0,0)
        
                
        
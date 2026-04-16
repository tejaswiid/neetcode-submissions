class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}
        def dfs(total,i):
            if total > amount or i == len(coins):
                return 0
            if total == amount:
                return 1 
            if (total,i) in dp: return dp[(total,i)]
            val = 0
            for j in range(i,len(coins)):
                c = coins[j]
                val += dfs(total+c,j)
            dp[(total,i)] = val
            return val
        return dfs(0,0)
        
                
        
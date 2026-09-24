class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}
        def dfs(i,total):
            if total == 0: return 1
            if i == len(coins) or total < 0: return 0
            #use the coin
            if (i,total) in dp: return dp[(i,total)]
            dp[(i,total)] = dfs(i,total-coins[i])
            #skip the coin
            dp[(i,total)] += dfs(i+1,total)
            return dp[(i,total)]
        return dfs(0,amount)
        
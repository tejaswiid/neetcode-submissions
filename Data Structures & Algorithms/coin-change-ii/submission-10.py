class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}
        def dfs(i,total):
            # print(i,total)
            if total == amount: return 1
            if i == len(coins) or total > amount:
                return 0
            if (i,total) in dp: return dp[(i,total)]
            res = 0
            for j in range(i,len(coins)):
                res += dfs(j,total+coins[j])
            dp[(i,total)] = res
            return res
        return dfs(0,0)
            
        
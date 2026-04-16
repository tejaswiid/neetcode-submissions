class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = {0:0}
        coins.sort(reverse=True)
        def dfs(amount):
            if amount in dp: return dp[amount]
            res = float("inf")
            for c in coins:

                if amount >= c:
                    val = dfs(amount - c)
                    if val != -1:
                        res = min(res, 1 + val)
            if res == float("inf"): res = -1
            dp[amount] = res
            # print(amount,dp[amount])
            return res

        return dfs(amount)

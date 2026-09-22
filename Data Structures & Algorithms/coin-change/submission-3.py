class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        for c in coins:
            dp[c] = 1
        def dfs(amount):
            if amount == 0: return 0
            if amount in dp: return dp[amount]
            dp[amount] = float("inf")
            for c in coins:
                if amount >= c:
                    dp[amount] = min(dp[amount],1+dfs(amount-c))
            return dp[amount]
        val = dfs(amount)
        return val if val != float("inf") else -1
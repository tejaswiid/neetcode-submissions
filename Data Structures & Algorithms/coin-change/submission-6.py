class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        dp = {}
        def dfs(remain):
            if remain == 0:
                return 0
            if remain in dp: return dp[remain]
            val = float("inf")
            for i in range(len(coins)):
                if coins[i] <= remain:
                    val = min(val,1+dfs(remain-coins[i]))
            dp[remain] = val
            return val
        res = dfs(amount)
        return res if res != float("inf") else -1
        

        
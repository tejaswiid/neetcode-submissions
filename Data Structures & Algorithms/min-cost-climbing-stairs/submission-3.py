class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        self.res = float("inf")
        dp = {}
        def dfs(i):
            if i >= len(cost):
                dp[i] = 0
                return 0
            if i in dp: return dp[i]
            dp[i] = cost[i]
            dp[i] += min(dfs(i+1),dfs(i+2))
            return dp[i]
        return min(dfs(0),dfs(1))


        
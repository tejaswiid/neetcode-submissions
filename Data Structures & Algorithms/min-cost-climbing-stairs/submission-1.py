class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = {}
        dp[len(cost)-1] = cost[-1]
        dp[len(cost)] = 0
        
        def dfs(i):
            if i in dp:
                return dp[i]
            dp[i] = cost[i] + min(dfs(i+1),dfs(i+2))
            return dp[i]
            
        val1, val2 = dfs(0), dfs(1)
        
        return min(val1,val2)


        
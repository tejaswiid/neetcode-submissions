class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        dp = {}
        dp[0], dp[1] = nums[0], max(nums[1],nums[0])
        
        def dfs(i):
            if i in dp: return dp[i]
            dp[i] = max(nums[i]+dfs(i-2),dfs(i-1))
            return dp[i]
        return dfs(len(nums)-1)
        
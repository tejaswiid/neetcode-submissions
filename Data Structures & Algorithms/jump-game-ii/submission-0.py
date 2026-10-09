class Solution:
    def jump(self, nums: list[int]) -> int:
        dp = {}
        dp[len(nums)-1] = 0
        for i in range(len(nums)-2,-1,-1):
            val = float("inf")
            for j in range(i+1,i+nums[i]+1):
                if j < len(nums):
                    val = min(val,1 + dp[j])
            dp[i] = val
        return dp[0]
            
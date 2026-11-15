class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        
        def dfs(i):
            if i >= len(nums):
                dp[i] = 0
                return 0
            if i in dp: return dp[i]
            dp[i] = max(dfs(i+1),nums[i]+dfs(i+2))
            return dp[i]
        nums1,nums2 = nums[:-1],nums[1:]
        nums = nums1
        dp = {}
        res = dfs(0)
        nums = nums2
        # print(nums1,nums2)
        dp = {}
        res = max(res,dfs(0))
        return res
            

        
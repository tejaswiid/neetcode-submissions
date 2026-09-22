class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        def linear(nums):
            if len(nums) == 1: return nums[0]
            dp = {}
            def dfs(i):
                if i < 0: return 0
                if i in dp: return dp[i]
                dp[i] = max(nums[i]+dfs(i-2),dfs(i-1))
                return dp[i]
            return dfs(len(nums)-1)
        nums1, nums2 = nums[1:], nums[:-1]
        print(nums1,nums2)
        return max(linear(nums1),linear(nums2))
        
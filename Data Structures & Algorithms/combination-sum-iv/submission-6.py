class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        self.res = 0
        dp = {target:1}
        def dfs(total):
            if total == target:
                
                return 1
            if total > target:
                return 0
            if total in dp: return dp[total]
            res = 0
            for i in range(len(nums)):
                if total + nums[i] <= target:
                   res += dfs(total+nums[i])
            dp[total] = res
            return res
        return dfs(0)
        


        
        
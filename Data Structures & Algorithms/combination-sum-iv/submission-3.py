class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        dp = {target:1}
        def dfs(total):
            if total in dp: return dp[total]
            res = 0
            for n in nums:
                if total + n > target:
                    break
                res += dfs(n+total)
            dp[total] = res
            return res
        return dfs(0)


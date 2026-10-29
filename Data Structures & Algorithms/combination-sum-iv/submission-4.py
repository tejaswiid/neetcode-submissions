class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        res = 0
        dp = {}
        def dfs(i,val):
            if val == target:
                dp[(i,val)] = 1
                return 1
            if val > target:
                dp[(i,val)] = 0
                return 0
            if (i,val) in dp: return dp[(i,val)]
            res = 0
            for j in range(i,len(nums)):
                val += nums[j]
                res += dfs(i,val)
                val -= nums[j]
            dp[(i,val)] = res
            return res
        return dfs(0,0)
        
                

        
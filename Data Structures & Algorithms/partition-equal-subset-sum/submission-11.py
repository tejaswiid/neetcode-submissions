class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2: return False
        nums.sort()
        total = sum(nums) // 2
        dp = {}
        def dfs(i,total):
            if (i,total) in dp:
                return  dp[(i,total)]
            if total == 0: return True
            if total < 0: return False
            if i == len(nums): return False
            dp[(i,total)] = False
            
            val1 = dfs(i+1,total-nums[i])
            val2 = dfs(i+1,total)
            dp[(i,total)] = val1 or val2
            return dp[(i,total)]
        return dfs(0,total)
        
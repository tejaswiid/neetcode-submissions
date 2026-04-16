class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2: return False
        target = sum(nums) // 2
        def dfs(i,summ):
            if summ == target: return True
            if i == len(nums): return False
            val1 = dfs(i+1,summ+nums[i])
            val2 = dfs(i+1,summ)
            if val1 or val2: return True
            else: return False
        return dfs(0,0)


        
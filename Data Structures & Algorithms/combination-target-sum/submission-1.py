class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i,subsets,total):
            if total == target:
                res.append(subsets.copy())
                return 
            if total > target or i == len(nums):
                return 
            subsets.append(nums[i])
            dfs(i,subsets,total+nums[i])
            subsets.pop()
            dfs(i+1,subsets,total)
        dfs(0,[],0)
        return res

        
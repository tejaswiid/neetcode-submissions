class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subsets = []
        def dfs(i):
            if i > len(nums) - 1:
                res.append(subsets.copy())
                return 
            subsets.append(nums[i])
            dfs(i+1)
            subsets.pop()
            dfs(i+1)
            return 
        dfs(0)
        return res


        
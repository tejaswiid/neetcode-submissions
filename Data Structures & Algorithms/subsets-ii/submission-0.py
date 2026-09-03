class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(i,subsets):
            if i == len(nums):
                vals = subsets.copy()
                vals.sort()
                if vals not in res: res.append(vals)
                return 

            subsets.append(nums[i])
            dfs(i+1,subsets)
            subsets.pop()
            dfs(i+1,subsets)
        dfs(0,[])
        return res
        
        
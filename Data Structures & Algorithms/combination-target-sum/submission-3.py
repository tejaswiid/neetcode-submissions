class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i,total,subsets):
            if total == target:
                res.append(subsets.copy())
                return 
            if i == len(nums) or total > target:
                return  
            subsets.append(nums[i])
            dfs(i,total+nums[i],subsets)
            subsets.pop()
            dfs(i+1,total,subsets)
            return 
        dfs(0,0,[])
        return list(res)


        
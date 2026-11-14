class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(start,subsets):
            # print(subsets)
            if sum(subsets) == target:
                # print(subsets)
                res.append(subsets.copy())
                return 
            if sum(subsets) > target:
                return 
            for i in range(start,len(nums)):
                subsets.append(nums[i])
                dfs(i,subsets)
                subsets.pop()
                # dfs(subsets)
            return 
        dfs(0,[])
        return res


        
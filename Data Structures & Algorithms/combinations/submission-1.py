class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1,n+1)]
        res = []
        def dfs(i,subsets):
            if len(subsets) == k:
                res.append(subsets.copy())
                return
            if i == len(nums): return 
            subsets.append(nums[i])
            dfs(i+1,subsets)
            subsets.pop()
            dfs(i+1,subsets)
            return 
        dfs(0,[])
        return res


        
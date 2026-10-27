class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1,n+1)]
        print(nums)
        res = []
        def dfs(i,subsets):
            if i == len(nums) and len(subsets) == k:
                res.append(subsets.copy())
                # subsets.pop()
                return 
            if i >= len(nums): return 
            subsets.append(nums[i])
            dfs(i+1,subsets)
            subsets.pop()
            dfs(i+1,subsets)
            return 
        dfs(0,[])
        return res
    # 1 2 3 

    # 1 2 

        
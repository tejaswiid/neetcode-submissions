class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        seen = set()
        def dfs(i,subsets):
            if i == len(nums):
                subsets.sort()
                if tuple(subsets) not in seen:
                    seen.add(tuple(subsets.copy()))
                    res.append(subsets.copy())
                return 
            subsets.append(nums[i])
            dfs(i+1,subsets)
            subsets.pop()
            dfs(i+1,subsets)
            return 
        dfs(0,[])
        return res

        
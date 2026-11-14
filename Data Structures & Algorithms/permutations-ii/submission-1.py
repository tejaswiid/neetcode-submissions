class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        seen = set()
        nums.sort()
        def dfs(nums,subsets):
            if not nums:
                if tuple(subsets) not in seen:
                    seen.add(tuple(subsets.copy()))
                    res.append(subsets.copy())
                return 
            for i in range(len(nums)):
                val = nums[i]
                subsets.append(nums[i])
                nums.pop(i)
                dfs(nums,subsets)
                subsets.pop()
                nums.insert(i,val)
            return 
        dfs(nums,[])
        return res


            

        
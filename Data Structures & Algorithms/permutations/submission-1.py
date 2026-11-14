class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(nums,subsets):
            # print(nums,subsets)
            if not nums:
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




        
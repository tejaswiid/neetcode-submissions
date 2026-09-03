class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(nums,subsets):
            if len(nums) == 1:
                subsets.append(nums[0])
                res.append(subsets.copy())
                subsets.pop()
                return 
            for i in range(len(nums)):
                subsets.append(nums[i])
                nums2 = nums.copy()
                nums2.pop(i)
                dfs(nums2,subsets)
                subsets.pop()
        dfs(nums,[])
        return res

                

                
        
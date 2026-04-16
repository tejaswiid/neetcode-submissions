class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        for i in range(len(nums)):
            till = before = nums[i]
            for j in range(i+1,len(nums)):
                before = before * nums[j]
                till = max(till, before, nums[j])
            res = max(res,till)
        return res
        
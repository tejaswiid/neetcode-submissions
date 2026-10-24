class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums) + 1
        res = 0
        for i in range(n):
            res = res ^ i
        for n in nums:
            res = res ^ n
        return res
            
        
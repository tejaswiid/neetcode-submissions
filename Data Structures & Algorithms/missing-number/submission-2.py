class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums) + 1
        nums = set(nums)
        for i in range(n):
            if i  not in nums: return i
        
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        res = 1
        nums.sort()
        for n in nums:
            if n > 0 and n == res:
                res += 1
        return res
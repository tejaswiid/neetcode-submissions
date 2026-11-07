class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l,r = 0, 0
        res = float("inf")
        while r <= len(nums):
            # print(l,r)
            while sum(nums[l:r]) >= target:
                res = min(res,r-l)
                l += 1
            r += 1
      
        return res if res != float("inf") else 0
        # 2 3 1 2 4 3


        
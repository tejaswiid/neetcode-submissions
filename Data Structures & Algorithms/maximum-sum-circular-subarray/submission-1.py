class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curmax, globmax,curmin, globmin = 0, nums[0], 0, nums[0]
        total = 0
        for n in nums:
            curmax = max(curmax+n,n)
            curmin = min(curmin+n,n)
            total += n
            globmax = max(globmax,curmax)
            globmin = min(globmin,curmin)
        return max(globmax,total-globmin) if globmax > 0 else globmax
        
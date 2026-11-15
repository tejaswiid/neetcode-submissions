class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        self.res = nums[0]
        maxp, minp = nums[0], nums[0]
        for i in range(1,len(nums)):
            val1 = nums[i]
            val2 = maxp * nums[i]
            val3 = minp * nums[i]
            maxp = max(val1,val2,val3)
            minp = min(val1,val2,val3)
            self.res = max(self.res,maxp)
        return self.res

        
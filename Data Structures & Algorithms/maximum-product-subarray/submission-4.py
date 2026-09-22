class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        self.res = nums[0]
        # def dfs(i,maxp,minp):
        #     if i == len(nums):
        #         return
        #     val1 = nums[i]
        #     val2 = maxp * nums[i]
        #     val3 = minp * nums[i]
        #     maxp = max(val1,val2,val3)
        #     minp = min(val1,val2,val3)
        #     print(maxp,minp)
        #     self.res = max(self.res,maxp)
        #     # print(self.res)
        #     dfs(i+1,maxp,minp)
        # dfs(1,nums[0],nums[0])
        # return self.res
        maxp, minp = nums[0], nums[0]
        for i in range(1,len(nums)):
            val1 = nums[i]
            val2 = maxp * nums[i]
            val3 = minp * nums[i]
            maxp = max(val1,val2,val3)
            minp = min(val1,val2,val3)
            self.res = max(self.res,maxp)
        return self.res

        
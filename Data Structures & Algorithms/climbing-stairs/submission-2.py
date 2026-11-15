class Solution:
    def climbStairs(self, n: int) -> int:
        nums = [1,1]
        for i in range(2,n+1):
            nums.append(nums[-1]+nums[-2])
        return nums[-1]
        
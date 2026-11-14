class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.res = 0

        def dfs(i,ans):
            if i == len(nums):
                self.res += ans
                return 
            ans ^= nums[i]
            dfs(i+1,ans)
            ans ^= nums[i]
            dfs(i+1,ans)
            return 
        dfs(0,0)
        return self.res




        
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        dp = {}
        def dfs(i,j):
            if i > j: return 0
            if (i,j) in dp: return dp[(i,j)]
            dp[(i,j)] = 0
            for ind in range(i+1,j):
                dp[(i,j)] = max(dp[(i,j)],nums[i]*nums[ind]*nums[j] + dfs(i,ind) + dfs(ind,j))
            return dp[(i,j)]
        
        return dfs(0,len(nums)-1)
                
        
        
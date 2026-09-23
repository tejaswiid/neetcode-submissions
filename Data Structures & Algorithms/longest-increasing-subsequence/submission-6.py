class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = {}
        def dfs(i,j):
            if i == len(nums):
                dp[(i,j)] = 0
                return 0
            if (i,j) in dp: return dp[(i,j)]
            dp[(i,j)] = dfs(i+1,j)
            if j == -1 or nums[i] > nums[j]:
                dp[(i,j)] = max(dp[(i,j)],1 + dfs(i+1,i))
            return dp[(i,j)]
        return dfs(0,-1)
            
            
                
                
        
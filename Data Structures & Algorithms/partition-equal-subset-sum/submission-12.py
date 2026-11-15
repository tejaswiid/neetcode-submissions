class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2: return False
        target = total //2
        nums.sort(reverse=True)
        sides = [0]*2
        def dfs(i):
            if i == len(nums):
                return sides[0] == sides[1]
            for k in range(2):
                if sides[k] + nums[i] <= target:
                    sides[k] += nums[i]
                    if dfs(i+1):
                        return True
                    sides[k] -= nums[i]
            return False
        return dfs(0)
            


        
class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        if sum(nums) % 4 != 0:
            return False

        nums.sort(reverse=True)
        target = sum(nums) // 4
        used = [False] * len(nums)

        def backtrack(i, k, subsetSum):
            if k == 0:
                return True
            if subsetSum == target:
                return backtrack(0, k - 1, 0)
            for j in range(i, len(nums)):
                if used[j] or subsetSum + nums[j] > target:
                    continue
                used[j] = True
                if backtrack(j + 1, k, subsetSum + nums[j]):
                    return True
                used[j] = False
            return False

        return backtrack(0, 4, 0)
        
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        sides = [0]*k
        total = sum(nums)
        if total % k: return False
        target = total // k
        nums.sort(reverse=True)
        if nums[0] > target: return False
        def areequal(nums):
            for i in range(1,len(nums)):
                if nums[i] != nums[i-1]:
                    return False
            return True
        
        def dfs(i):
            if i == len(nums):
                return areequal(sides)
            seen = set()
            for j in range(k):
                if sides[j] in seen: continue
                if sides[j] + nums[i] <= target:
                    seen.add(sides[j])
                    sides[j] += nums[i]
                    if dfs(i+1): return True
                    sides[j] -= nums[i]
                    if sides[j] == 0:
                        break
            return False
        return dfs(0)


        
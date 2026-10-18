class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        nums = list(set(nums))
        nums.sort()
        # 2 3 4 5 10 20
        res = 0
        l, r = 0, 0
        # print(nums)
        while l <= r and r+1 < len(nums):
            if nums[r] + 1 == nums[r+1]:
                r += 1
            else:
                res = max(res,r-l+1)
                l = r = r+1
        res = max(res,r-l+1)
        return res





        
        
    

        
        
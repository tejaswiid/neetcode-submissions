class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums) - 1
        while l <= r:
            m = (l+r) // 2
            if nums[m] == target:
                return m
            lef , rig= nums[m-1], nums[m]
            if lef < target < rig:
                return m
            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
        # print(l,r)
        return len(nums) if r == len(nums) - 1 else 0
            
            


            
             



        
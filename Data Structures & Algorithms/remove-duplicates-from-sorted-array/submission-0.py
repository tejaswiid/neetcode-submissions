class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums_set = list(set(nums))
        nums_set.sort()
        for i in range(len(nums)):
            if i >= len(nums_set):
                nums.pop()
                continue
            nums[i] = nums_set[i]
        
        return len(set(nums))
        
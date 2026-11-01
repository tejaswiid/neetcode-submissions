class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        vals = []
        new = []
        for i in range(len(nums)):
            if nums[i] == val:
                vals.append("_")
            else:
                new.append(nums[i])
        k = len(new)
        for i in range(len(nums)):
            if i < k:
                nums[i] = new[i]
            else:
                nums[i] = "_"
        return k

        
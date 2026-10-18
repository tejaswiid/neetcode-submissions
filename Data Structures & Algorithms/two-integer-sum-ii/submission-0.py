class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp = defaultdict(int)
        for i in range(len(nums)):
            n = nums[i]
            if n in comp:
                return [comp[n]+1,i+1]
            comp[target-n] = i
        

        
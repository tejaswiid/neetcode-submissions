class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp = {}
        for i,n in enumerate(nums):
            if n in comp:
               return [comp[n],i]
            comp[target-n] = i
            # print(comp)

        
        
            
        
        
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.res = 0
        def sumxor(arr):
            su = 0
            for a in arr:
                su ^= a
            return su

        def dfs(i,subsets):
            if i == len(nums):
                self.res += sumxor(subsets)
                return 
            subsets.append(nums[i])
            dfs(i+1,subsets)
            subsets.pop()
            dfs(i+1,subsets)
            return 
        dfs(0,[])
        return self.res


        
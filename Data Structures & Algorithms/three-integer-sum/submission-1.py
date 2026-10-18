class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twosum(arr,target):
            seen = set()
            pairs = []
            for i in range(len(arr)):
                if arr[i] in seen:
                    pairs.append([arr[i],target-arr[i]])
                seen.add(target-arr[i])
            return pairs
        res = set()
        for i,n in enumerate(nums):
            val = [n]
            arr = nums[:i] + nums[i+1:]
            ans = twosum(arr,-n)
            for pair in ans:
                triplet = tuple(sorted([n]+pair))
                res.add(triplet)
        return [list(t) for t in res]

            


        
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        maxx = 0
        res = 0
        for k,v in count.items():
            if v > maxx:
                res, maxx = k, v
        return res


        
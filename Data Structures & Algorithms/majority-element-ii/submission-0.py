class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        res = []
        n = len(nums) / 3
        for k,v in count.items():
            if v > n:
                res.append(k)
        return res

        
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prod = nums[0] if nums[0] != 0 else 1
        zs = 1 if nums[0] == 0 else 0
        zero = True if nums[0] == 0 else False
        for i in range(1,len(nums)):
            n = nums[i]
            if n != 0: 
                prod *= n
            if n == 0:
                zs += 1
        print(zs,prod)
        if zs > 1: return [0]*len(nums)
        if not zs:
            for n in nums:
                res.append(prod // n)
        elif zs == 1:
            for n in nums:
                if n == 0:
                    res.append(prod)
                else: res.append(0)
        return res

        # 1 2 4 6 
        # 1 2 8 48
        # 48 48 24 6 

        # -1 0 0 0 0 
        #  0 0 6 6 3


        
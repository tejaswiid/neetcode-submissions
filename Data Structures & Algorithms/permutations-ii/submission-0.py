class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(subsets,num):
            if not num:
                val = subsets.copy()
                if val not in res:
                    res.append(val)
                return 
            for j in range(len(num)):
                subsets.append(num[j])
                new_num = num[:j] + num[j+1:]
                dfs(subsets,new_num)
                subsets.pop()
        dfs([],nums)
        return res
            

        
        
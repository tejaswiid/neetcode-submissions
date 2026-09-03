class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(i,subsets,total):
            if total == target:
                res.append(subsets.copy())
                return 
            if total > target or i == len(candidates):
                return
            subsets.append(candidates[i])
            dfs(i+1,subsets,total+candidates[i])
            subsets.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1,subsets,total)
        dfs(0,[],0)
        return res
        
        
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(i,subsets,total):
            if total == target :
                res.append(subsets.copy())
                return 
            if i == len(candidates) or total > target:
                return 
            subsets.append(candidates[i])
            dfs(i+1,subsets,total+candidates[i])
            subsets.pop()
            j = i+1
            while j < len(candidates) and candidates[i] == candidates[j]:
                j += 1
            dfs(j,subsets,total)
            return 
        dfs(0,[],0)
        return res

        
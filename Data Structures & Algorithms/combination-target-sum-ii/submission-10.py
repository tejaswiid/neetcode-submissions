class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        def dfs(start,subsets,total):
            if total == target :
                ans.append(subsets.copy())
                return 
            if total > target:
                return 
            for i in range(start,len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                subsets.append(candidates[i])
                dfs(i+1,subsets,total+candidates[i])
                subsets.pop()
            return 
        dfs(0,[],0)
        return ans
            

        
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # 1 2 3 4 5
        # 1  
        # 12 13 14 15
        # 123 124 125
        # 1234 1235
        # 12345 
        
        # 2
        # 23 24 25
        # 234   245

        # 3
        # 34 35
        candidates.sort()
        res = []
        visit = set()
        def dfs(i,total,subsets):
            if total == target:
                res.append(subsets.copy()) 
                return 
            elif total > target or i == len(candidates):
                return 
            for j in range(i,len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue

                # Since sorted, everything after this is also too large
                if total + candidates[j] > target:
                    break
                
                subsets.append(candidates[j])
                dfs(j+1,total+candidates[j],subsets)
                subsets.pop()
                  
            return 
        dfs(0,0,[])
        return res



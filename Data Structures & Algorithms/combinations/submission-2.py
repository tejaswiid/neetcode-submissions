class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1,n+1)]
        res = []
        def dfs(start,subsets):
            if len(subsets) == k:
                res.append(subsets.copy())
                return
            for i in range(start,n+1):
                subsets.append(i)
                dfs(i+1,subsets)
                subsets.pop()
            return 
        dfs(1,[])
        return res


        
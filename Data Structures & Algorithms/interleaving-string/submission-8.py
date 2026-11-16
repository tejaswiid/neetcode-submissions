class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False
        dp = {}
        def dfs(i,j):
            if i + j == len(s3):
                return True
            if (i,j) in dp: return dp[(i,j)]
            if i < len(s1) and s3[i+j] == s1[i]:
                res = dfs(i+1,j)
                dp[(i,j)] = True
                if res: return True
            if j < len(s2) and s3[i+j] == s2[j]:
                res = dfs(i,j+1)
                dp[(i,j)] = True
                if res: return True
            dp[(i,j)] = False
            return False
        return dfs(0,0)
            




        
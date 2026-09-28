class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        lens1, lens2 = len(s1), len(s2)
        if lens1+lens2 != len(s3):
            return False
        
        dp = {}
        def dfs(i,j):
            if i+j == len(s3): return True
            if (i,j) in dp:
                return dp[(i,j)]
            dp[(i,j)] = False
            if i < len(s1) and s1[i] == s3[i+j]:
                if dfs(i+1,j): dp[(i,j)] = True
            if j < len(s2) and s2[j] == s3[i+j]:
                if dfs(i,j+1): dp[(i,j)] = True
            return dp[(i,j)]
        return dfs(0,0)

                
            
        
            
        
        
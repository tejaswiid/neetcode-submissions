class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = {}
        def dfs(i,j):
            if i == len(text1) or j == len(text2):
                dp[(i,j)] = 0
                return 0
            if (i,j) in dp: return dp[(i,j)]
            val = 0
            if text1[i] == text2[j]:
                val = max(val,1 + dfs(i+1,j+1))
            else:
                val = max(val,dfs(i+1,j),dfs(i,j+1))
            dp[(i,j)] = val
            return val
        return dfs(0,0)



        
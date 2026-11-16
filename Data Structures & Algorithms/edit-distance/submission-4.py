class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = {}
        def dfs(i,j):
            if i == len(word1) and j == len(word2):
                return 0
            if i == len(word1): return len(word2) - j
            if j == len(word2): return len(word1) - i
            if (i,j) in dp: return dp[(i,j)]
          
            res = float("inf")
            if word1[i] == word2[j]:
                res = min(res,dfs(i+1,j+1))
            else:
                #insert
                val1 = 1 + dfs(i,j+1)
                #delete
                val2 = 1 + dfs(i+1,j)
                #replace
                val3 = 1 + dfs(i+1,j+1)
                res = min(val1,val2,val3)
            dp[(i,j)] = res
            return res
        return dfs(0,0)


        
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}
        def dfs(i):
            if i == len(s):
                return True
            if i in dp: return dp[i]
            dp[i] = False
            for j in range(i+1,len(s)+1):
                if s[i:j] in wordDict:
                    if dfs(j):
                        dp[i] = True
                        return True
            return dp[i]
        return dfs(0)
        
class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[-1 for _ in range(len(s))] for _ in range(len(s))]
        def dfs(l,r):
            if l >= r:
                dp[l][r] = True
                return True
            if dp[l][r] != -1: return dp[l][r]
            dp[l][r] = False
            if s[l] == s[r]:
                dp[l][r] = dfs(l+1,r-1)
            return dp[l][r]
        ind, lenn = 0, 0
        for l in range(len(s)):
            for r in range(len(s)):
                if dfs(l,r):
                    if (r-l+1) > lenn:
                        lenn , ind = (r-l+1), l
        return s[ind:ind+lenn]

        
class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[-1 for _ in range(len(s))]for _ in range(len(s))]
        def dfs(l,r):
            if l >= r:
                dp[l][r] = True
                return True
            if dp[l][r] != -1: return dp[l][r]
            dp[l][r] = False
            if s[l] == s[r]:
                if dfs(l+1,r-1):
                    dp[l][r] = True
                    return True
            return dp[l][r]
        start,length = 0, 0
        for l in range(len(s)):
            for r in range(len(s)):
                if dfs(l,r):
                    if (r-l+1) > length:
                        length = (r-l+1)
                        start = l
        return s[start:start+length]
                


        
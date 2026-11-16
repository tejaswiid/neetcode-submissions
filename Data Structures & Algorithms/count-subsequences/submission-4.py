class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        def issame(s1,s2):
            if len(s1) != len(s2): return False
            for i in range(len(s1)):
                if s1[i] != s2[i]: 
                    return False
            return True
        dp = {}
        def dfs(st,i):
            if len(st) > len(s): return 0
            if issame(st,t): return 1
            if i == len(s): return 0
            if (st,i) in dp: return dp[(st,i)]
            val = 0
            st += s[i]
            val += dfs(st,i+1)
            st = st[:-1]
            val += dfs(st,i+1)
            dp[(st,i)] = val
            return val
        return dfs("",0)
        
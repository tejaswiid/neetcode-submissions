class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dic = defaultdict(list)
        dp = {len(s):True}
        for w in wordDict:
            dic[w[0]].append(w)
        print(dic)
        def issame(s1,s2):
            if len(s1) != len(s2): return False
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    return False
            return True
        def dfs(i):
            if i > len(s): return False
            if i == len(s): return True
            if i in dp: return dp[i]
            val = False
            print(s[i])
            if s[i] not in dic.keys(): return False
            for w in dic[s[i]]:
                l = len(w)
                print(w,s[i])
                if l <= len(s) and issame(s[i:i+l],w):
                    if dfs(i+l): val = True
            dp[i] = val
            return val
        return dfs(0)
        
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ""
        if not len(t): return ""
        countT = Counter(t)
        window = {}
        have, need = 0, len(countT)
        res, resLen = [-1,-1], float("inf")
        r, l = 0 , 0
        while r < len(s):
            window[s[r]] = 1 + window.get(s[r],0)
            if s[r] in countT and window[s[r]] == countT[s[r]]:
                have += 1
            while have == need:
                if r-l+1 < resLen:
                    res, resLen = [l,r], r-l+1
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
            r += 1
        l,r = res
        return s[l:r+1] if resLen != float("inf") else ""


    






        
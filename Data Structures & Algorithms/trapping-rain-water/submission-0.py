class Solution:
    def trap(self, height: List[int]) -> int:
        pref, suf = [-1],[-1]
        for i in range(len(height)):
            if height[i] > pref[-1]:
                pref.append(height[i])
            else:
                pref.append(pref[-1])
        for i in range(len(height)-1,-1,-1):
            if height[i] > suf[-1]:
                suf.append(height[i])
            else:
                suf.append(suf[-1])
        suf = suf[::-1]
        res = 0
        for i in range(len(height)):
            val = min(suf[i],pref[i]) - height[i]
            if val > 0: res += val
        return res






        
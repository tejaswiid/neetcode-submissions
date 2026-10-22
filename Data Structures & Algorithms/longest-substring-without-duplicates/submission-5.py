class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 
        r = 1
        if s == "": return 0
        if s == " ": return 1 
        res = 1
        while l <= r and r < len(s):
            while s[r] in s[l:r]:
                l += 1
            res = max(res,r-l+1)
            r += 1
                
            
        return res 

        
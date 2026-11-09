class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check(l,r):
            while l < r:
                if s[l] != s[r]:
                    return False
                else:
                    l += 1 
                    r -= 1
            return True
        
        l , r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return check(l,r-1) or check(l+1,r)
            else:
                l += 1
                r -= 1
        return True
            
        
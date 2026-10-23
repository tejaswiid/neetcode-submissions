class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def isperm(s1,s2):
            s1,s2 = sorted(s1), sorted(s2)
            if len(s1) != len(s2): return False
            for i in range(len(s1)):
                if s1[i] != s2[i]: 
                    return False
            return True
        l , r = 0, len(s1)
        while r <= len(s2):
            if isperm(s1,s2[l:r]):
                return True
            l += 1
            r += 1
        return False
            
        
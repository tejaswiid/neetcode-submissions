class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        f = strs[0]
        res = ""

        for i in range(1,len(f)+1):
            yes = True
            for s in strs:
                if f[:i] != s[:i]:
                    yes = False
                    break
            if yes: 
                res = f[:i]
            else:
                break
        return res

        
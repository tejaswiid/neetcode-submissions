class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        words = set(wordDict)
        def dfs(i,val):
            if i == len(s):
                res.append(" ".join(val))
                return 
            for j in range(i+1,len(s)+1):
                word = s[i:j]
                if word in words:
                    val.append(word)
                    dfs(j,val)
                    val.pop()
        dfs(0,[])
        return res
        
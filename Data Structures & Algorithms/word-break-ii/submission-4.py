class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        def dfs(i,val):
            # print(i,val)
            if i == len(s):
                res.append(" ".join(val))
                return 
            for j in range(i+1,len(s)+1):
                if s[i:j] in wordDict:
                    val.append(s[i:j])
                    dfs(j,val)
                    val.pop()
            return 
        dfs(0,[])
        return res


        
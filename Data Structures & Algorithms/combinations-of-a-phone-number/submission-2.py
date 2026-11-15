class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        res = []
        count = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}

        def dfs(i,word):
            if i == len(digits):
                res.append("".join(word))
                return 
            st = count[digits[i]]
            for s in st:
                word.append(s)
                dfs(i+1,word)
                word.pop()
            return 
        dfs(0,[])
        return res
            
            





        
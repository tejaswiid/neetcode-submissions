class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {"2":"abc", "3": "def", "4":"ghi", "5":"jkl","6":"mno", "7":"pqrs", "8": "tuv", "9":"wxyz" }
        if digits == "": return  []
        res = []
        def dfs(digits,string):
            if digits == "":
                res.append("".join(string))
                return 
            first = digits[0]
            act = dic[first]
            for f in act:
                string.append(f)
                new = digits[1:]
                dfs(new,string)
                string.pop()
        dfs(digits,[])
        return res



        
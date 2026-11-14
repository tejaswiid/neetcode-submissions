class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def ispal(s):
            return s == s[::-1]
        def dfs(form,remain):
            # print(form,remain)
            if not remain:
                res.append(form.copy())
                return 
            for i in range(1,len(remain)+1):
                val = remain[:i]
                if ispal(val):
                    form.append(val)
                    if i < len(remain):new_remain = remain[i:] 
                    else: new_remain = None
                    dfs(form,new_remain)
                    form.pop()
            return 
        dfs([],s)
        return res

        
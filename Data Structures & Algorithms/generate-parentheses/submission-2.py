class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def isitvalid(s):
            op,cl = 0,0
            for s in s:
                if s == "(":
                    op += 1
                elif s == ")":
                    cl += 1
            return op,cl
        res = []
        def dfs(stack):
            if len(stack) == 2*n:
                res.append("".join(stack))
                return
            op,cl = isitvalid(stack)
            if op < n:
                stack.append("(") 
                dfs(stack)
                stack.pop()
            if cl < op and cl < n:
                stack.append(")")
                dfs(stack)
                stack.pop()
            return 

        dfs([])
        return res
            






        
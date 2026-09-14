class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def opcl(stack):
            op, cl = 0,0
            for s in stack:
                if s == "(": op += 1
                elif s == ")": cl += 1
            return op,cl
        def dfs(stack):
            if len(stack) == n*2:
                res.append("".join(stack))
                return 
            op,cl = opcl(stack)
            if op < n: 
                stack.append("(")
                dfs(stack)
                stack.pop()
            if op > cl and cl < n:
                stack.append(")")
                dfs(stack)
                stack.pop()
        dfs([])
        return res
            
            
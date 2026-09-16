class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        vals = ["+","-","*","/"]
        for t in tokens:
            if t not in vals:
                stack.append(t)
            elif t in vals:
                a, b = int(stack.pop()), int(stack.pop())
                if t == "+": res = a+b
                elif t == "-": res = b - a
                elif t == "*": res = a*b
                else: res = b / a
                print(res)
                stack.append(res)
        return int(stack[0])
        
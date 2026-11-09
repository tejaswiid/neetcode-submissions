class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for st in s:
            if st == "]":
                val = ""
                while stack and stack[-1] != "[":
                    val = stack.pop() + val
                stack.pop()
                n = ""
                while stack and stack[-1] in "0123456789":
                    n += stack.pop()
                # print(n)
                n = int(n[::-1])
            
                if val: 
                    res = ""
                    for _ in range(n):
                        res += val
                    stack.append(res)
            else:
                stack.append(st)
        return "".join(stack)




        
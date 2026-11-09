class Solution:
    def simplifyPath(self, path: str) -> str:
        arr = path.split("/")
        stack = []
        for a in arr:
            if a == "":
                continue
            elif a == ".":
                continue
            elif a == "..":
                if stack:
                    stack.pop()
            else:
                stack.append("/"+a)
        s = "".join(stack)
        # print(arr,stack,s)
        return s if s else "/"

            


        
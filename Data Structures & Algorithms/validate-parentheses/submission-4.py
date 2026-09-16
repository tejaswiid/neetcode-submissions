class Solution:
    def isValid(self, s: str) -> bool:
        dic = {")":"(","}":"{","]":"["}
        stack = []
        for s in s:
            if s in dic:
                if not stack:
                    return False
                elif dic[s] != stack[-1]:
                        return False
                else:
                    stack.pop()
            else:
                stack.append(s)
        return True if not stack else False

        
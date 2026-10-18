class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        new = ""
        for s in s:
            if s in "abcdefghijklmnopqrstuvwxyz" or s in "0123456789":
                new += s
        # print(new)
        return new == new[::-1]
        
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen:
            seen.add(n)
            n = str(n)
            su = 0
            for i in n:
                su += int(i)*int(i)
            n = su
        return True if 1 in seen else False


        
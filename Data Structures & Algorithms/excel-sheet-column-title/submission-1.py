class Solution:
    def convertToTitle(self, n: int) -> str:
        count = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        res = ""
        while n > 26:
            # print(n)
            v = n % 26 
            res += count[v]
            n = n // 26
        res += count[n]
        return res[::-1]

        
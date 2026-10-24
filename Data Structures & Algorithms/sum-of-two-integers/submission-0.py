class Solution:
    def getSum(self, a: int, b: int) -> int:
        xo = a ^ b
        n = (a&b) << 1
        return xo + n

        
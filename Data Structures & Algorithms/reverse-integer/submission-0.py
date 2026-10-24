class Solution:
    def reverse(self, x: int) -> int:
        neg = False
        if x < 0: neg = True
        x = abs(x)
        x = str(x)
        x = int(x[::-1])
        if not ((-2)**31 <= x <= (2)**31 - 1):
            return 0
        return -x if neg else x
    
        
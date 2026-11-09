class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def convert(a):
            n = 0 
            a = a[::-1]
            for i in range(len(a)):
                n += (2**i) * int(a[i])
            return n
        num = convert(a) + convert(b)
        return str(bin(num))[2:]
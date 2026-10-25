class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def convert(num):
            n, i = 0,0
            while i < len(num):
                n = n * 10 + int(num[i])
                i += 1
            return n
        n1, n2 = convert(num1), convert(num2)
        res = n1*n2
        return str(res)
        
            
        
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def dfs(x,n):
            if n == 0: return 1
            if n == 1: return x

            if n % 2:
                val = dfs(x,n//2)
                return x*val*val
            else:
                val = dfs(x,n//2)
                return val*val
        if n < 0: 
            val = dfs(x,-n)
        else: val = dfs(x,n)
        return float(val) if n > 0 else 1/float(val)
        
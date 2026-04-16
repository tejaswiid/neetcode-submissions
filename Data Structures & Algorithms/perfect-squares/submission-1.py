class Solution:
    def numSquares(self, n: int) -> int:
        l = math.sqrt(n)
        l = int(l)
        def gen(l):
            arr = []
            for i in range(1,l+1):
                arr.append(i*i)
            return arr
        arr = gen(l)
        dp = {0:0}
        def dfs(rem):
            if rem in dp : return dp[rem]
            res = float("inf")
            for a in arr:
                if rem < a:
                    break
                res = min(res,1 + dfs(rem-a))
            dp[rem] = res
            return res
        return dfs(n)
                

            
        

        
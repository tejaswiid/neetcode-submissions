class Solution:
    def numSquares(self, n: int) -> int:
        squares = []
        i = 1
        while i*i <= n:
            squares.append(i*i)
            i += 1
        target = n
        squares.sort(reverse=True)
        dp = {}
        def dfs(total):
            if total == target:
                return 0
            if total in dp: return dp[total]
            res = float("inf")
            for i in range(len(squares)):
                if total + squares[i] <= target:
                    res = min(res,1+dfs(total+squares[i]))
            dp[total] = res
            return res
        return dfs(0)
        



        
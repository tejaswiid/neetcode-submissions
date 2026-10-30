class Solution:
    def integerBreak(self, n: int) -> int:
        nums = []
        for i in range(n-1,0,-1):
            nums.append(i)
        res = 0 
        dp = {}
        def dfs(summ,vals):
            if summ == n:
                dp[(summ,vals)] = vals
                return vals
            if (summ,vals) in dp: return dp[(summ,vals)]
            ans = 0
            for num in nums:
                if num + summ > n:
                    continue
                summ += num
                vals *= num
                ans = max(ans,dfs(summ,vals))
                summ -= num
                vals //= num
            dp[(summ,vals)] = ans
            return ans
        return dfs(0,1)

    





        

        
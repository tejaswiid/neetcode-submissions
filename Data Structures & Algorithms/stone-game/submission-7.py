class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = {}
        def dfs(l,r,alice):
            if l > r: return 0
            if (l,r) in dp: return dp[(l,r)]
            if alice:
                val1 = piles[l] + dfs(l+1,r,not alice)
                val2 = piles[r] + dfs(l,r-1,not alice)
                res = max(val1,val2)
            else:
                val1 = piles[l] + dfs(l+1,r,not alice)
                val2 = piles[r] + dfs(l,r-1,not alice)
                res = min(val1,val2)
            dp[(l,r)] = res
            return res
        alice = dfs(0,len(piles)-1,True)
        bob = sum(piles) - alice
        return True if alice > bob else False


        
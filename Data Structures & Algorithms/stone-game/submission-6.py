class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = {}
        def dfs(l,r,alice):
            if l > r:
                return 0
            if (l,r) in dp: return dp[(l,r)]
            if alice:
                val1, val2 = piles[l] + dfs(l+1,r,not alice), piles[r] +dfs(l,r-1,not alice)
                dp[(l,r)] =  max(val1,val2)
                return dp[(l,r)]
            else:
                val1, val2 = piles[l] + dfs(l+1,r,not alice), piles[r] +dfs(l,r-1,not alice)
                dp[(l,r)] = min(val1,val2)
                return dp[(l,r)]
        alice = dfs(0,len(piles)-1,True)
        bob = sum(piles) - alice
        return True if alice > bob else False
        

        
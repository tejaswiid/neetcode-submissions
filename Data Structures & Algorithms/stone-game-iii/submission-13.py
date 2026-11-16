class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        dp = {}
        def dfs(i,alice):
            if i == len(stoneValue):
                return 0 
            if (i,alice) in dp: return dp[(i,alice)]
            res = float("-inf") if alice else float("inf")
            for j in range(i,min(i+3,len(stoneValue))):
                if alice:
                    val = sum(stoneValue[i:j+1]) + dfs(j+1,not alice)
                    res = max(res,val)
                else:
                    val = dfs(j+1,not alice)
                    res = min(res,val)
            dp[(i,alice)] = res
            return res
        alice = dfs(0,True)
        bob = sum(stoneValue) - alice
        if alice > bob: return "Alice"
        elif bob > alice: return "Bob"
        else: return "Tie"
                

        
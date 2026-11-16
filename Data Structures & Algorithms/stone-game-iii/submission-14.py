class Solution:
    def stoneGameIII(self, stones: List[int]) -> str:
        dp = {}
        def dfs(alice,i):
            if i == len(stones):
                return 0
            if (alice,i) in dp: return dp[(alice,i)]
            res = float("-inf") if alice else float("inf")
            for j in range(i,min(i+3,len(stones))):
                if alice:
                    val = sum(stones[i:j+1]) + dfs(not alice,j+1)
                    res = max(res,val)
                else:
                    val = dfs(not alice,j+1)
                    res = min(res,val)
            dp[(alice,i)] = res
            return res
        alice = dfs(True,0) 
        bob = sum(stones) - alice
        if alice > bob: return "Alice" 
        elif bob> alice: return "Bob"
        else: return "Tie"

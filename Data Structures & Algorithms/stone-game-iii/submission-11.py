class Solution:
    def stoneGameIII(self, stones: List[int]) -> str:
        dp = {}
        def dfs(alice,i):
            if i == len(stones):
                return 0
            if (alice,i) in dp: return dp[(alice,i)]
            total = 0
            res = float("-inf") if alice else float("inf")
            for j in range(i,min(i+3,len(stones))):
                total += stones[j]
                if alice:
                    res = max(res,total + dfs(not alice,j+1))
                else:
                    res = min(res,dfs(not alice,j+1))
            dp[(alice,i)] = res
            return res
        alice = dfs(True,0)
        bob = sum(stones) - alice
        if alice > bob: 
            return "Alice"
        elif alice < bob:
            return "Bob"
        else:
            return "Tie"
                    



        
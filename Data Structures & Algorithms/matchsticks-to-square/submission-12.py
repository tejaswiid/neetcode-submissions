class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total % 4: return False
        target = total // 4
        squares = [0]*4
        matchsticks.sort(reverse=True)
        def dfs(squares,i):
            if i == len(matchsticks):
                # print(squares)
                return squares[0] == squares[1] == squares[2] == squares[3] == target
            for j in range(4):
                if squares[j] + matchsticks[i] <= target:
                    squares[j] += matchsticks[i]
                    if dfs(squares,i+1): return True
                    squares[j] -= matchsticks[i]
            return False
        return dfs(squares,0)
        
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones) > 1:
            x,y = stones.pop(), stones.pop()
            if x != y:
                stones.append(abs(x-y))
            stones.sort()
        return stones[0] if stones else 0



        
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
             return False
        hand.sort()
        dic = Counter(hand)
        for h in hand:
            if dic[h]:
                for j in range(h,h+groupSize):
                    if not dic[j]: 
                        return False
                    dic[j] -= 1
        return True
        







        
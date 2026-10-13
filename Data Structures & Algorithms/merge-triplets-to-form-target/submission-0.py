class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = []
        for t1,t2,t3 in triplets:
            if t1 > target[0] or t2 > target[1] or t3 > target[2]:
                continue
            good.append([t1,t2,t3])
        t1,t2,t3 = False,False,False
        for f1,f2,f3 in good:
            if target[0] == f1: t1 = True
            if target[1] == f2: t2 = True
            if target[2] == f3: t3 = True
        return t1 and t2 and t3

        
                






        
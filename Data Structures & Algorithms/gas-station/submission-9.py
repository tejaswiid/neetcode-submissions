class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        comb = []
        for g,c in zip(gas,cost):
            comb.append(g-c)
        if sum(comb) < 0: return -1
        maxi = float("-inf")
        res = 0
        n = len(comb)
        comb = comb + comb
        
        for i in range(n):
            if comb[i] > 0:
                start, res = i, comb[i]
                val = True
                for j in range(i+1,i+n):
                    if res + comb[j] < 0:
                        val = False
                        break
                    res += comb[j]
                print(start,val)
                if val: return i
        return 0
        # n = 4 
        #   0 1  2  3 4 5. 6. 7 
        # # -1 3 -4 2 -1 3 -4 2 



        


        
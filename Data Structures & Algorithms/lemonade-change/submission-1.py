class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives, tens = 0, 0
        for b in bills:
            if b == 5:
                fives += 1
            elif b == 10:
                if fives:
                    fives -= 1
                else: return False
                tens +=1 
            elif b == 20:
                change = b - 5
                if  fives >0 and tens > 0:
                    fives -= 1
                    tens -= 1
                elif fives >= 3:
                    fives -= 3

                
                else:
                    return False
        return True
            


            

        
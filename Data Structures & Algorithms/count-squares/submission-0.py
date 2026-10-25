class CountSquares:

    def __init__(self):
        self.pcount = defaultdict(int)


        

    def add(self, point: List[int]) -> None:
        point = tuple(point)
        self.pcount[point] += 1

        

    def count(self, point: List[int]) -> int:
        res = 0
        p1,p2 = point
        for po,k in self.pcount.items():
            po1,po2 = po
            if po1 != p1 and po2 != p2 and abs(po1-p1) == abs(po2-p2):
                val = k
                val *= self.pcount.get((po1,p2),0)
                val *= self.pcount.get((p1,po2),0)
                res += val
            
        return res



            
        

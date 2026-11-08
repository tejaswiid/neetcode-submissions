class StockSpanner:

    def __init__(self):
        self.stack = []
        

    def next(self, price: int) -> int:
        res = 1
        new = self.stack.copy()
        while new and price >= new[-1]:
            res += 1
            new.pop()
        self.stack.append(price)
        return res
        
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
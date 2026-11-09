class FreqStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        

    def pop(self) -> int:
        count = Counter(self.stack)
        maxfre, res = 0, 0
        for i in range(len(self.stack)-1,-1,-1):
            if count[self.stack[i]] > maxfre:
                maxfre = count[self.stack[i]]
                res = self.stack[i]
                ind = i 
        self.stack.pop(ind)
        return res

        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
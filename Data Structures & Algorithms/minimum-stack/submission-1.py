class MinStack:

    def __init__(self):
        self.MinStack = []
        self.mini = []

        

    def push(self, val: int) -> None:
        self.MinStack.append(val)
        if len(self.mini) == 0:
            self.mini.append(val)
        elif self.mini[-1] > val:
            self.mini.append(val)
        else:
            self.mini.append(self.mini[-1])
        
        

        

    def pop(self) -> None:
        self.MinStack.pop()
        self.mini.pop()

        
        

    def top(self) -> int:
        return self.MinStack[-1]

        

    def getMin(self) -> int:
       return self.mini[-1]

        

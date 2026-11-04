class MyHashMap:

    def __init__(self):
        self.keys = []
        self.values = []
        

    def put(self, key: int, value: int) -> None:
        if key not in self.keys:
            self.keys.append(key)
            self.values.append(value)
        else:
            for i in range(len(self.keys)):
                if key == self.keys[i]:
                    self.values[i] = value
                    break
        

    def get(self, key: int) -> int:
        for i in range(len(self.keys)):
            if key == self.keys[i]:
                return self.values[i]
        return -1
        
        

    def remove(self, key: int) -> None:
        for i in range(len(self.keys)):
            if key == self.keys[i]:
                self.keys.pop(i)
                self.values.pop(i)
                break
        
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
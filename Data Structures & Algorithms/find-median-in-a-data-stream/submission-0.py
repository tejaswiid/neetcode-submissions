class MedianFinder:

    def __init__(self):
        self.median = []
        

    def addNum(self, num: int) -> None:
        self.median.append(num)
        self.median.sort()
        

    def findMedian(self) -> float:
        l = len(self.median)
        if l % 2: 
            return self.median[l//2]
        else:
            mid = l // 2
            return (self.median[mid]+self.median[mid - 1]) / 2
        
        
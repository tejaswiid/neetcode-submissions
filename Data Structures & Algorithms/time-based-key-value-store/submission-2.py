class TimeMap:

    def __init__(self):
        self.TimeMap = defaultdict(list)
        
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.TimeMap[key].append((timestamp,value))

        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.TimeMap: return ""
        vals = self.TimeMap[key]

        
        l, r = 0, len(vals) - 1
        # vals.sort()
        res = ""
        # print(vals)
        while l <= r:
            m = (l+r) // 2
            if timestamp < vals[m][0]:
                r = m - 1
            elif timestamp > vals[m][0]:
                res = vals[m][1]
                l = m + 1
            else:
                return vals[m][1]
        
        return res


        

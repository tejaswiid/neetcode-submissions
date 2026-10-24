class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
        for i in range(1,len(intervals)): 
            f1, l1 = res[-1]
            pf, pl = intervals[i][0], intervals[i][1]
            if  pf <= l1:
                res[-1][1] = max(pl,l1)
            else:
                res.append(intervals[i])
   
        return res

        
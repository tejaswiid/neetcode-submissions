class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        comp = intervals[0][1]
        for i in range(1,len(intervals)):
            i1,i2 = intervals[i]
            if comp > i1:
                res += 1
                comp = min(comp,i2)
            else:
                comp = i2
        return res
            

        
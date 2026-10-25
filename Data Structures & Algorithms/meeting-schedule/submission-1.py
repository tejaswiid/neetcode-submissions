"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        new = []
        for i in intervals:
            i1,i2 = i.start,i.end
            new.append([i1,i2])
        new.sort()
        if not new: return True
        comp = new[0][1]
        for i1,i2 in new[1:]:
            if i1 < comp:
                return False
            comp = max(comp,i2)
        return True

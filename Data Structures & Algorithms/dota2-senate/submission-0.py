class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        qr, qd  = deque(), deque()
        for i,s in enumerate(senate):
            if s == "R":qr.append(i)
            if s == "D":qd.append(i)
        n = len(senate)
        while qr and qd:
            r = qr.popleft()
            d = qd.popleft()
            if r < d:
                qr.append(r+n)
            else:
                qd.append(d+n)
        if qr: return "Radiant"
        if qd: return "Dire"       
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        q = deque()
        q.append("0000")
        visit = set()
        visit.add("0000")
        val = 0
        while q:
            for _ in range(len(q)):
                dig = q.popleft()
                if int(dig) == int(target):
                    return val
                for i in range(4):
                    n = int(dig[i])
                    inc =  dig[:i] + str((n+1) % 10) + str(dig[i+1:])
                    dec = dig[:i]+ str((n-1+10) % 10) + str(dig[i+1:])
                    # print(inc,dec)
                    if inc not in visit and inc not in deadends: 
                        q.append(inc)
                        visit.add(inc)
                    if dec not in visit and dec not in deadends:
                        q.append(dec)
                        visit.add(dec)
            val += 1
        return -1
                
                    
                    




        
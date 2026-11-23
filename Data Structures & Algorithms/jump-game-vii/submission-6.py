class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        q = deque()
        q.append(0)
        farthest = 0
        n = len(s)
        visit = set()
        visit.add(0)
        while q:
            v = q.popleft()
            start = max(v+minJump,farthest+1)
            end = min(n-1,v+maxJump)
            visit.add(v)
            for j in range(start,end+1):
                if s[j] == "0" and j not in visit:
                    if j == n-1: return True
                    q.append(j)
            farthest = max(farthest,end)
        return False


            
        
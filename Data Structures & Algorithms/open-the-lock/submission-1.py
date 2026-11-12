class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends or target in deadends:
            return -1
        q, visit = deque(), set()
        q.append("0000")
        visit.add("0000")
        val = 0
        while q:
            for _ in range(len(q)):
                num = q.popleft()
                if num == target:
                    return val
                # print(num)
                for i in range(4):
                    n = int(num[i])
                    inc = num[:i] + str((n+1) % 10) + num[i+1:]
                    dec = num[:i] + str((n-1+10) % 10) + num[i+1:]
                    if inc not in visit and inc not in deadends:
                        q.append(inc)
                        visit.add(inc)
                    if dec not in visit and dec not in deadends:
                        q.append(dec)
                        visit.add(dec)
            val += 1
        return -1

        
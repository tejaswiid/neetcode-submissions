class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        adj = defaultdict(list)
        for t1,t2 in trust:
            adj[t1].append(t2)
        nob = -1
        for i in range(1,n+1):
            if i not in adj:
                nob = i
                break
        for i in range(1,n+1):
            if i != nob:
                if nob not in adj[i]:
                    return -1

        return nob
       
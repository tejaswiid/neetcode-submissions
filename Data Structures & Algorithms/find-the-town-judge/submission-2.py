class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        adj = defaultdict(list)
        radj = defaultdict(list)
        for t1,t2 in trust:
            adj[t2].append(t1)
            radj[t1].append(t2)
        for i in range(1,n+1):
            if len(adj[i]) == n-1 and i not in radj:
                return i
        return -1
        
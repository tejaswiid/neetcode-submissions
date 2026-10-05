class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        tickets.sort()
        for t1,t2 in tickets:
            adj[t1].append(t2)
        for k in adj:
            adj[k].sort()
        res = []
        def dfs(node):
            while adj[node]:
                nei = adj[node][0]
                adj[node].remove(nei)
                dfs(nei)
            res.append(node)
        dfs("JFK")
        return res[::-1]
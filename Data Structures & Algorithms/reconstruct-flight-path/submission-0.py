class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for t1,t2 in tickets:
            adj[t1].append(t2)
        for t in adj:
            adj[t].sort(reverse=True)
        res = []
        def dfs(node):
            while adj[node]:
                nei = adj[node].pop()
                dfs(nei)
            res.append(node)
            return 
        dfs("JFK")
        return res[::-1]


        
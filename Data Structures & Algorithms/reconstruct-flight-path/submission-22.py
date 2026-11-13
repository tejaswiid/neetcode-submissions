class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for t1,t2 in tickets:
            adj[t1].append(t2)
        

        for k,v in adj.items():
            v.sort()
        res = []
        def dfs(node):
            while adj[node]:
                nei = adj[node][0]
                adj[node].pop(0)
                dfs(nei)
            res.append(node)
            return 
        dfs("JFK")
        return res[::-1]
        

            
            
        

        
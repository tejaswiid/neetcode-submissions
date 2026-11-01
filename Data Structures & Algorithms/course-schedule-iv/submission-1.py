class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        adj = defaultdict(list)

        for n1, n2 in prerequisites:
            adj[n1].append(n2)

        pre = defaultdict(set)

        def dfs(node):
            for nei in adj[node]:
                if nei not in pre[node]:
                    pre[node].add(nei)
                    dfs(nei)
                    pre[node].update(pre[nei])

        for n in range(numCourses):
            dfs(n)

        res = []
        for q1, q2 in queries:
            res.append(q2 in pre[q1])

        return res
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)
        prereq = defaultdict(set)
        for p1,p2 in prerequisites:
            adj[p2].append(p1)
        def dfs(node):
            if node in prereq:
                return prereq[node]
            prereq[node].add(node)
            for nei in adj[node]:
                prereq[node].update(dfs(nei))
            
            return prereq[node]
        res = []
        for n in range(numCourses):
            if n not in prereq:
                dfs(n)
        # print(prereq)
        for q1,q2 in queries:
            if q1 in prereq[q2]:
                res.append(True)
            else: res.append(False)
        return res
                


            
            
        
        
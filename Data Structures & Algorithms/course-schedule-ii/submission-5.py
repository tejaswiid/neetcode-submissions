class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for p1,p2 in prerequisites:
            adj[p1].append(p2)
        visit = set()
        res = []
        def dfs(course,cycle):
            if course in cycle:
                return False
            if course in visit:
                return True
            cycle.add(course)
            for crs in adj[course]:
                if not dfs(crs,cycle):
                    return False
            cycle.remove(course)
            visit.add(course)
            res.append(course)
            return True
        for n in range(numCourses):
            if n not in visit:
                if not dfs(n,set()):
                    return []
        return res if len(visit) == numCourses else []
            

        
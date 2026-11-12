class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for p1,p2 in prerequisites:
            adj[p1].append(p2)
        visit = set()
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
            return True
        for n in range(numCourses):
            if n not in visit:
                dfs(n,set())
        print(visit)
        return len(visit) == numCourses


        
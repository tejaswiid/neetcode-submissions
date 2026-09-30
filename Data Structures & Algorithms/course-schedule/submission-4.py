class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for p1,p2 in prerequisites:
            adj[p1].append(p2)
        visit = set()
        done = set()
        def dfs(course):
            if course in visit: return False
            if course in done: return True
            visit.add(course)
            for pre in adj[course]:
                if not dfs(pre):
                    return False
            visit.remove(course)
            done.add(course)
            return True
            
                        
            
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True



        
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visit = set()
        done = set()
        adj = defaultdict(list)
        for p1,p2 in prerequisites:
            adj[p1].append(p2)
        
        def dfs(course):
            if course in visit:
                return False
            if course in done:
                return True
            visit.add(course)
            for nei in adj[course]:
                if not dfs(nei):
                    return False
            visit.remove(course)
            done.add(course)
            res.append(course)
            return True
        
        res = []
        for i in range(numCourses):
            if not dfs(i):
                return []
            
        return res 
        
                


            
        
        
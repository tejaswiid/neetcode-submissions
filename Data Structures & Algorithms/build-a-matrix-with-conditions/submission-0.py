class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        adjr = defaultdict(list)
        adjc = defaultdict(list)
        for r1,r2 in rowConditions:
            adjr[r1].append(r2)
        for c1,c2 in colConditions:
            adjc[c1].append(c2)
        
        self.res = []
        def dfs(adj,n):
            
            if n in path:
                return False
            if n in visit:
                return True
            path.add(n)
            for nei in adj[n]:
                if not dfs(adj,nei):
                    return False
            path.remove(n)
            visit.add(n)
            self.res.append(n)
            return True
        visit = set()
        path = set()
        for i in range(1, k + 1):
            if not dfs(adjr, i):
                return []
        rows = self.res[::-1]
        visit = set()
        path = set()
        for i in range(1, k + 1):
            if not dfs(adjc, i):
                return []
        cols = self.res[::-1]


        grid = [[0 for _ in range(k)] for _ in range(k)]
        for i in range(1,k+1):
            r = rows.index(i)
            c = cols.index(i)
            grid[r][c] = i
        return grid

        
      
            



        
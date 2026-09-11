class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def ispal(st):
            rev = st[::-1]
            for i in range(len(st)):
                if st[i] != rev[i]:
                    return False
            return True

        def dfs(s,subsets):
            if len(s) == 1:
                subsets.append(s)
                res.append(subsets.copy())
                subsets.pop()
                return 
            if len(s) == 0:
                res.append(subsets.copy())
                return
            for i in range(1,len(s)+1):
                st = s[:i]
                if ispal(st):
                    subsets.append(st)
                    dfs(s[i:],subsets)
                    subsets.pop()
            return 
        dfs(s,[])
        return res
        
                

            
                
            

            
        
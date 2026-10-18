class Solution:
    
    
    def encode(self, strs: List[str]) -> str:
        self.keys = []
        res = ""
        start = 0
        for s in strs:
            start += len(s)
            self.keys.append(start)
            res += s
        return res


    def decode(self, s: str) -> List[str]:
        res = []
        prev = 0
  
        for i in self.keys:
            val = s[prev:i]
            prev = i
            res.append(val)
        
        return res
        

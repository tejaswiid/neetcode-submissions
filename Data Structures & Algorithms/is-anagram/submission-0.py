class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        s_dic, t_dic = {}, {}
        for val in s:
            s_dic[val] = 1 + s_dic.get(val,0)
        for val in t:
            t_dic[val] = 1 + t_dic.get(val,0)
        
        for val in s:
            if val not in t_dic:
                return False
            
            if s_dic[val] != t_dic[val]: 
                return False

        return True
         
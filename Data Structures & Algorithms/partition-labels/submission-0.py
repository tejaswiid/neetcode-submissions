class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # x y x x y z b z b b i s l
        # 0 1 2 3 4 5 6 7 8 9 10 11 12

        res = []
        dic = defaultdict(int)
        for i,v in enumerate(s):
            dic[v] = i
        l = 0
        while l < len(s):
            r = dic[s[l]]
            i = l+1
            while i < r:
                if dic[s[i]] > r:
                    r = dic[s[i]]
                i += 1
            res.append(r-l+1)
            l = r+1
        return res



        
        
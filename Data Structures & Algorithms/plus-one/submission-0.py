class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        st = ""
        for d in digits:
            st += str(d)
        st = int(st) + 1
        st = str(st)
        res = []
        for s in st:
            res.append(int(s))
        return res
        
class Solution:
    def checkValidString(self, s: str) -> bool:
        low, high = 0, 0 
        for v in s:
            if v == "(": 
                low += 1
                high += 1
            if v == ")":
                low = max(0,low-1)
                high -= 1
            if v == "*":
                low = max(0,low-1)
                high += 1
            if high < 0: return False
        return low == 0
        



  
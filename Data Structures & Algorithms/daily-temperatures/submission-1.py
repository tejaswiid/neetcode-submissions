class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)
        # print(res)
        for i,t in enumerate(temperatures):
            if not stack:
                stack.append([t,i])
            else:
                while stack and  t > stack[-1][0]:

                    num, ind = stack.pop()
                    res[ind] = i - ind
                stack.append([t,i])
        return res


        
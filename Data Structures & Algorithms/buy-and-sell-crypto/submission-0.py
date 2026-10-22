class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pre , post = [float("inf")],[float("-inf")]
        for p in prices:
            if pre[-1] > p:
                pre.append(p)
            else:
                pre.append(pre[-1])
        prices = prices[::-1]
        for p in prices:
            if post[-1] < p:
                post.append(p)
            else:
                post.append(post[-1])
    
        post.pop(0)
        pre.pop(0)
        post = post[::-1]
        # print(pre,post)

        res = float("-inf")
        for i in range(len(post)):
            res = max(res,post[i]-pre[i])
        return res


        
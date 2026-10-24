class Solution:
    def reverseBits(self, n: int) -> int:
        res = ""
        for i in range(32):
            if (1 << i) & n:
                res += "1"
            else: res += "0"
        res = res[::-1]
        ans = 0
        for i in range(len(res)):
            ans += int(res[i]) * (2**i)
        return ans

        
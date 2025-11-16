class Solution:
    def numSub(self, s: str) -> int:
        mod = 10**9+7
        cur, res = 0, 0
        for x in s+'0':
            if x == '1':
                cur += 1
            else:
                res += cur * (cur + 1) // 2 % mod
                cur = 0
        return res
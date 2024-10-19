class Solution:
    def getLucky(self, s: str, k: int) -> int:
        cur = ''.join([str(ord(x)-96) for x in s])
        for i in range(k):
            res = 0
            for x in cur:
                res += int(x)
            cur = str(res)
        return int(cur)
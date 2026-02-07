class Solution:
    def minimumDeletions(self, s: str) -> int:
        res = len(s)
        a = s.count('a')
        b = 0

        for c in s:
            a -= (c == 'a')
            res = min(res, a + b)
            b += (c == 'b')

        return res

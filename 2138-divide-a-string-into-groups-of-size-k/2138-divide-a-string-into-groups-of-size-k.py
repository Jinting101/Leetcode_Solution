class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        n = len(s)
        rest = 0
        if n % k:
            rest = (n // k + 1) * k - n
        s = s + fill*rest
        res = []
        for i in range(0, n, k):
            res.append(s[i:i+k])
        return res
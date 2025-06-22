class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        left = len(s) % 3
        rest = fill*2 if left == 1 else fill if left == 2 else ''
        s = s + rest
        res = []
        for i in range(0, len(s), 3):
            res.append(s[i:i+3])
        return res
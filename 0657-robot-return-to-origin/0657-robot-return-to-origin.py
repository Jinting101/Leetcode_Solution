class Solution:
    def judgeCircle(self, moves: str) -> bool:
        u, d, l, r = 0, 0, 0, 0
        for x in moves:
            if x == "U":
                u += 1
            elif x == "D":
                d += 1
            elif x == "L":
                l += 1
            else:
                r += 1
        return u == d and l == r
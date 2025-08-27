class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        res = 0
        curmax = 0
        for x, y in dimensions:
            cur = math.sqrt(x**2 + y**2)
            if cur == curmax:
                res = max(res, x*y)
            elif cur > curmax:
                curmax = cur
                res = x*y
        return res
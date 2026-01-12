class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res = 0
        n = len(points)
        for i in range(1, n):
            a,b = points[i-1]
            x,y = points[i]
            res += max(abs(x-a), abs(y-b))
        return res

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        q = []
        res, l = 0, 0
        for x, y in classes:
            res += x/y
            l += 1
            z = (-((x+1)/(y+1)-x/y), x, y)
            heapq.heappush(q, z)
        for i in range(extraStudents):
            cur, x, y = heapq.heappop(q)
            res -= x / y
            x, y = x + 1, y + 1
            res += x / y
            z = (-((x+1)/(y+1)-x/y), x, y)
            heapq.heappush(q, z)
        return res / l

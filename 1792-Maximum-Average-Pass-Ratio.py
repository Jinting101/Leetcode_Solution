class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        q = []
        for x, y in classes:
            z = (-((x+1)/(y+1)-x/y), x, y)
            heapq.heappush(q, z)
        for i in range(extraStudents):
            cur, x, y = heapq.heappop(q)
            x, y = x + 1, y + 1
            z = (-((x+1)/(y+1)-x/y), x, y)
            heapq.heappush(q, z)
        res, l = 0, 0
        while q:
            cur, x, y = heapq.heappop(q)
            res += x/y
            l += 1
        return res / l

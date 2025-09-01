class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        hp = []
        avg = 0
        for x,y in classes:
            heapq.heappush(hp, (x/y - (x+1)/(y+1), x, y))
            avg += x/y
        for _ in range(extraStudents):
            acc, x, y = heapq.heappop(hp)
            nx, ny = x+1, y+1
            heapq.heappush(hp, (nx/ny - (nx+1)/(ny+1), nx, ny))
            avg -= (x/y - nx/ny)
        return avg / len(hp)
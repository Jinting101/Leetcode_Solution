class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        pq = []
        heapq.heappush(pq, (0, 0, 0))
        visited = [[0]*n for _ in range(m)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while pq:
            cost, i, j = heapq.heappop(pq)
            if visited[i][j]:
                continue
            if i == m-1 and j== n-1:
                return cost
            visited[i][j] = 1
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and not visited[ni][nj]:
                    new_cost = max(cost, abs(heights[ni][nj] - heights[i][j]))
                    heapq.heappush(pq, (new_cost, ni, nj))
        return -1

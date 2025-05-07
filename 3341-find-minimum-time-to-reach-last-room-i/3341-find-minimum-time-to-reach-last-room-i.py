class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = [[0]*m for _ in range(n)]
        q = [(0, 0, 0)]
        while q:
            curtime, r, c = heapq.heappop(q)
            if r == n-1 and c == m-1:
                return curtime
            for i, j in directions:
                nr, nc = r + i, c + j
                if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc]:
                    visited[nr][nc] = 1
                    heapq.heappush(q, (max(moveTime[nr][nc] + 1, curtime + 1), nr, nc))

        return -1

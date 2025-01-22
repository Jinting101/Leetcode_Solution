class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
        grid = [[-1]*n for i in range(m)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        pos = deque()
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    grid[i][j] = 0
                    pos.append((i,j))
        while pos:
            l = len(pos)
            for _ in range(l):
                i,j = pos.popleft()
                val = grid[i][j]
                for dx, dy in directions:
                    nr, nc = i+dx, j+dy
                    if not (0<=nr<m and 0<=nc<n and grid[nr][nc]==-1):
                        continue
                    pos.append((nr, nc))
                    grid[nr][nc] = val + 1
        return grid
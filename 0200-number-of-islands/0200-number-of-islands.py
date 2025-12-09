class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[0]*n for _ in range(m)]
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        res = 0
        
        def bfs(r, c):
            q = deque()
            visited.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]

                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if 0 <= r < m and 0 <= c < n and not visited[nr][nc] and grid[r][c] == "1":
                        q.append((r, c))
                        visited.add((r, c))

        def dfs(r, c):
            visited[r][c] = 1
            for i,j in directions:
                nr, nc = r + i, c + j
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc] and grid[nr][nc] == "1":
                    dfs(nr, nc)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and not visited[i][j]:
                    dfs(i, j)
                    res += 1

        return res



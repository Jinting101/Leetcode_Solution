class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[0]*n for _ in range(m)]
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        res = 0

        def dfs(r, c):
            for i,j in directions:
                nr, nc = r + i, c + j
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc] and grid[nr][nc] == "1":
                    visited[nr][nc] = 1
                    dfs(nr, nc)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and not visited[i][j]:
                    dfs(i, j)
                    res += 1

        return res



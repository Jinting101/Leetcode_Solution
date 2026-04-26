class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        visited = [[0]*n for _ in range(m)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(i, j, pi, pj):
            visited[i][j] = 1
            for dr, dc in directions:
                ni, nj = i + dr, j + dc
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == grid[i][j]:
                    if not visited[ni][nj]:
                        if dfs(ni, nj, i, j):
                            return True
                    elif (ni, nj) != (pi, pj):
                        return True
            return False

        for i in range(m):
            for j in range(n):
                if not visited[i][j]:
                    if dfs(i, j, -1, -1):
                        return True

        return False
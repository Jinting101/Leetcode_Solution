class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        m, n = len(grid), len(grid[0])
        visited = [[0]*n for _ in range(m)]
        
        def dfs(r, c, temp):
            temp[0] += 1
            visited[r][c] = 1
            for i, j in directions:
                nr = r + i
                nc = c + j
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc] and grid[nr][nc] == 1:
                    dfs(nr, nc, temp)
        
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == 1:
                    temp = [0]
                    dfs(i, j, temp)
                    res = max(res, temp[0])
        
        return res
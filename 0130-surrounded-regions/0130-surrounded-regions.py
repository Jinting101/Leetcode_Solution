class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = [[0] * n for _ in range(m)]

        def dfs(r, c):
            visited[r][c] = 1
            for i, j in directions:
                nr = r + i
                nc = c + j
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc] and board[nr][nc] == "O":
                    # visited[nr][nc] = 1
                    dfs(nr, nc)
        
        for i in range(m):
            for j in range(n):
                if (i == 0 or i == m-1 or j == 0 or j == n-1) and not visited[i][j] and board[i][j] == "O":
                    dfs(i, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O" and not visited[i][j]:
                    board[i][j] = "X"


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[0]*n for i in range(m)]
        res = 0
        for i in range(m):
            cur = []
            num = 0
            for j in range(n):
                if grid[i][j] == 1:
                    num += 1
                    cur.append((i,j))
                    visited[i][j] = 1
            res += num
            if num == 1:
                x,y = cur.pop()
                visited[x][y] = 0
                res -= 1
                
        for i in range(n):
            num = 0
            seen = 0
            for j in range(m):
                if grid[j][i] == 1:
                    num += 1
                    if visited[j][i]:
                        seen += 1
            if num > 1:
                res += num - seen

        return res
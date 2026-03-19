class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        res = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                topx, topy = 0, 0
                if i > 0:
                    topx, topy = map(int, grid[i-1][j].split('#'))
                leftx, lefty = 0, 0
                if j > 0:
                    leftx, lefty = map(int, grid[i][j-1].split('#'))
                prevx, prevy = 0, 0
                if i > 0 and j > 0:
                    prevx, prevy = map(int, grid[i-1][j-1].split('#'))
                curx = 1 if grid[i][j] == "X" else 0
                cury = 1 if grid[i][j] == "Y" else 0
                grid[i][j] = str(curx+topx+leftx-prevx) + "#" + str(cury+topy+lefty-prevy)
                temp = grid[i][j].split("#")
                if temp[0] == temp[1] and temp[0] != "0":
                    res += 1
        return res
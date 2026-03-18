class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                top = 0 if i == 0 else grid[i-1][j]
                left = 0 if j == 0 else grid[i][j-1]
                above = 0 if (i == 0 or j == 0) else grid[i-1][j-1]
                grid[i][j] += top + left - above
                if grid[i][j] <= k:
                    res += 1
        return res
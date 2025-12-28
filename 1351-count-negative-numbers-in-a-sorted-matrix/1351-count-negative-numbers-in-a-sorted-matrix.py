class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        i, j = m-1, 0
        res = 0
        while 0 <= i < m and 0 <= j < n:
            if grid[i][j] >= 0:
                j += 1
            else:
                if i == 0 or grid[i-1][j] < 0:
                    res += n - j
                    i -= 1
                else:
                    j += 1
                    res += 1
        return res

# 4. 3  3. 1
# 3. 2. -1 -1
# 1. 1. -1 -2
# -1 -1 -2 -3
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        total = 0
        rows = [0] * m
        cols = [0] * n
        for i in range(m):
            for j in range(n):
                rows[i] += grid[i][j]
                cols[j] += grid[i][j]
                total += grid[i][j]
        prev = rows[0]
        for i in range(1, m):
            if prev * 2 == total:
                return True
            prev += rows[i]
        prev = cols[0]
        for i in range(1, n):
            if prev * 2 == total:
                return True
            prev += cols[i]
        return False
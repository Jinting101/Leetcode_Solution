class Solution:
    def areSimilar(self, grid: List[List[int]], k: int) -> bool:
        m, n = len(grid), len(grid[0])
        for i in range(m):
            if i % 2 == 0:
                for j in range(n):
                    if grid[i][j] != grid[i][(j-k) % n]:
                        return False
            else:
                for j in range(n):
                    if grid[i][j] != grid[i][(j+k) % n]:
                        return False
        return True
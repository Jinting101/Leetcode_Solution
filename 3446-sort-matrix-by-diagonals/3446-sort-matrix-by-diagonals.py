class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        for i in range(n-1):
            cur = [grid[i+j][j] for j in range(n-i)]
            cur.sort(reverse=True)
            for j in range(n-i):
                grid[i+j][j] = cur[j]
        for i in range(1, n-1):
            cur = [grid[j][i+j] for j in range(n-i)]
            cur.sort()
            for j in range(n-i):
                grid[j][i+j] = cur[j]
        return grid

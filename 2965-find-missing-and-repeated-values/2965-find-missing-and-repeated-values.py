class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        seen = set(range(1, n*n+1))
        res = []
        for i in range(n):
            for j in range(n):
                x = grid[i][j]
                if x in seen:
                    seen.remove(grid[i][j])
                else:
                    res.append(x)
        return res + list(seen)
class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        if rows < 3 or cols < 3:
            return 0
        res = 0
        for i in range(2, rows):
            for j in range(2, cols):
                square = [grid[a][j-2:j+1] for a in range(i-2, i+1)]
                target = sum(square[0])
                diag1 = sum(square[i][i] for i in range(3))
                diag2 = sum(square[i][2-i] for i in range(3))
                if target != sum(square[1]) or target != sum(square[2]) or target != sum(square[k][0] for k in range(3)) or target != sum(square[k][1] for k in range(3)) or target != sum(square[k][2] for k in range(3)) or target != diag1 or target != diag2:
                    continue
                seen = set()
                for row in square:
                    for x in row:
                        seen.add(x)
                if seen == {1, 2, 3, 4, 5, 6, 7, 8, 9}:
                    res += 1
        return res
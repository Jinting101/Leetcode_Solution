class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def check(i, j, l):
            if i + l - 1 >= m or j + l - 1 >= n:
                return False
            mat = [grid[r][j:j+l] for r in range(i, i+l)]
            rs = sum(mat[0])
            for row in mat:
                if sum(row) != rs:
                    return False
            cols = [[mat[c][r] for c in range(l)] for r in range(l)]
            for col in cols:
                if sum(col) != rs:
                    return False
            diags = [mat[r][r] for r in range(l)]
            invdiags = [mat[r][l-r-1] for r in range(l)]
            if sum(diags) != rs or sum(invdiags) != rs:
                return False
            
            return True
        
        res = 1
        temp = min(m, n)
        for i in range(m):
            for j in range(n):
                for k in range(2, temp + 1):
                    if check(i, j, k):
                        res = max(res, k)
        return res
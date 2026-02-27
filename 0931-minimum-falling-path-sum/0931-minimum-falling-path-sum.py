class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        if n == 1:
            return matrix[0][0]
        res = float('inf')
        directions = [(-1, -1), (-1, 0), (-1, 1)]
        for i in range(1, n):
            for j in range(n):
                cur_min = float('inf')
                for di, dj in directions:
                    prev_i, prev_j = i + di, j + dj
                    if 0 <= prev_i < n and 0 <= prev_j < n:
                        cur_min = min(cur_min, matrix[prev_i][prev_j])
                matrix[i][j] += cur_min
                if i == n-1:
                    res = min(res, matrix[i][j])
        return res
        

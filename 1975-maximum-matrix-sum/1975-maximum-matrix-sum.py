class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        neg_cnt = 0
        zreo_cnt = 0
        res = 0
        neg_min = float('inf')
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == 0:
                    zreo_cnt += 1
                else:
                    neg_min = min(neg_min, abs(matrix[i][j]))
                if matrix[i][j] < 0:
                    neg_cnt += 1
                res += abs(matrix[i][j])
        if neg_cnt % 2 == 1 and not zreo_cnt:
            return res - 2 * neg_min
        return res
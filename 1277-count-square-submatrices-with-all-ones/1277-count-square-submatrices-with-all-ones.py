class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        # res = 0
        # m, n = len(matrix), len(matrix[0])
        # max_size = min(m, n)
        # dp = matrix[:]
        # for i in range(m):
        #     for j in range(n):
        #         if dp[i][j] >= 1:
        #             res += 1
        #             if i-1>=0 and j-1>=0:
        #                 for k in range(1, min(max_size, min(i,j)+1)):
        #                     if dp[i-1][j] >= k and dp[i][j-1]>=k and dp[i-1][j-1]>=k:
        #                         dp[i][j] = k + 1
        #                         res += 1
        # return res
        
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        total_squares = 0
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    if i == 0 or j == 0:
                        dp[i][j] = 1  # On edges, a single '1' forms a 1x1 square
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    total_squares += dp[i][j]

        return total_squares
    
# DP Matrix Definition:
    # Let dp[i][j] represent the size of the largest square submatrix with all ones that ends at cell ((i, j)).
    # If matrix[i][j] is zero, then dp[i][j] should be zero because we can't form a square submatrix ending in a cell with a zero.
    
# Transition Formula:
    # If matrix[i][j] is one, then:
    # [
    # dp[i][j] = \min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
    # ]
    # This formula works because the size of the square ending at ((i, j)) is limited by the smallest square ending to its left, top, or top-left diagonal cells.

# Summing up Squares:
    # Each dp[i][j] represents the side length of the largest square ending at ((i, j)).
    # The number of squares ending at ((i, j)) is equal to dp[i][j] itself.
    # Accumulate all values in the dp matrix to get the total count of square submatrices.
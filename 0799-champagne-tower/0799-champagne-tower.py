class Solution:
    def champagneTower(self, poured, query_row, query_glass):
        dp = [poured]
        for row in range(1, query_row + 1):
            new_row = [0.0] * (row + 1)
            for j in range(row):
                overflow = max(0, dp[j] - 1)
                new_row[j] += overflow / 2
                new_row[j + 1] += overflow / 2
            dp = new_row
        return min(1.0, dp[query_glass])
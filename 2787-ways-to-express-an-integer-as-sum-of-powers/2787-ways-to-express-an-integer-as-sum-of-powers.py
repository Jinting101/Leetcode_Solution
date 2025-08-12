class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 10**9 + 7
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(1, n + 1):
            val = i**x
            for j in range(n + 1):
                if j < val:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = (dp[i-1][j] + dp[i - 1][j - val]) % MOD
        return dp[n][n]
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        dp = [[[None] * (maxMove + 1) for _ in range(n)] for _ in range(m)]
        self.m = m
        self.n = n
        self.mod = 10**9 + 7
        return self.helper(maxMove, startRow, startColumn, dp)

    def helper(self, maxMove, x, y, dp):
        if x < 0 or x >= self.m or y < 0 or y >= self.n:
            return 1
        if maxMove <= 0:
            return 0
        if dp[x][y][maxMove] is not None:
            return dp[x][y][maxMove]
        res = 0

        res = (res + self.helper(maxMove - 1, x + 1, y, dp)) % self.mod
        res = (res + self.helper(maxMove - 1, x, y - 1, dp)) % self.mod
        res = (res + self.helper(maxMove - 1, x - 1, y, dp)) % self.mod
        res = (res + self.helper(maxMove - 1, x, y + 1, dp)) % self.mod

        dp[x][y][maxMove] = res

        return res


        # moves=[(1, 0), (-1,0), (0, 1), (0,-1)]
        # @cache
        # def f(i, j, moveLeft):
        #     if i<0 or i==m or j<0 or j==n: return 1
        #     if moveLeft==0: return 0
        #     ans=0
        #     for a, b in moves:
        #         ans=(ans+f(i+a, j+b, moveLeft-1))%(10**9+7)
        #     return ans
        # return f(startRow, startColumn, maxMove)


        # res = 0
        # dic = {}
        # directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        # for i in range(maxMove):
        #     if i == 0:
        #         for dr, dc in directions:
        #             r, c = startRow + dr, startColumn + dc
        #             if 0 <= r < m and 0 <= c < n:
        #                 if i+1 not in dic:
        #                     dic[i+1] = []
        #                 dic[i+1].append((r,c))
        #             else:
        #                 res += 1
        #     elif i in dic:
        #         for r, c in dic[i]:
        #             for dr, dc in directions:
        #                 nr = r + dr
        #                 nc = c + dc
        #                 if 0 <= nr < m and 0 <= nc < n:
        #                     if i+1 not in dic:
        #                         dic[i+1] = []
        #                     dic[i+1].append((nr,nc))
        #                 else:
        #                     res += 1
            
        # return res
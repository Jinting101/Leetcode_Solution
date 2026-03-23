class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        res = [['0']*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    res[i][j] = str(grid[i][j])
                elif i == 0:
                    res[i][j] = str(grid[i][j] * int(res[i][j-1]))
                elif j == 0:
                    res[i][j] = str(grid[i][j] * int(res[i-1][j]))
                else:
                    above = res[i-1][j]
                    left = res[i][j-1]
                    tmp = list(map(int, left.split("#"))) + list(map(int, above.split("#")))
                    lst = set([grid[i][j] * x for x in tmp])
                    if len(lst) == 1:
                        res[i][j] = str(min(lst))
                    else:
                        res[i][j] = str(min(lst)) + "#" + str(max(lst))
        ans = max(list(map(int, res[-1][-1].split("#"))))
        if ans < 0:
            return -1
        return ans % MOD

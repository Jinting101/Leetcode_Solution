class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        lu, ll, ru, rl = m+1, 0, m+1, 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    lu = min(lu, i)
                    ll = max(ll, i)
                    ru = min(ru, j)
                    rl = max(rl, j)
        return (ll-lu+1) * (rl-ru+1)
            

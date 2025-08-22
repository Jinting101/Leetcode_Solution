class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        lu, ll, ru, rl = float('inf'), 0, float('inf'), 0
        lst = []
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    lst.append((i, j))
        for x,y in lst:
            lu = min(lu, x)
            ll = max(ll, x)
            ru = min(ru, y)
            rl = max(rl, y)
        return (ll-lu+1) * (rl-ru+1)
            

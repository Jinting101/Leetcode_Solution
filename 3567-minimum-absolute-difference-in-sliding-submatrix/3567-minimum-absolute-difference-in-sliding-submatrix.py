class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        res = [[0]*(n-k+1) for _ in range(m-k+1)]
        if k == 1:
            return res

        for i in range(m-k+1):
            for j in range(n-k+1):
                temp = [row[j:j+k] for row in grid[i:i+k]]
                mat = list(set([x for row in temp for x in row]))
                mat.sort()
                l = len(mat)
                if l == 1:
                    continue
                res[i][j] = min([mat[p]-mat[p-1] for p in range(1, l)])

        return res

        

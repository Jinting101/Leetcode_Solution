class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        P = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                P[i][j] = (
                    P[i - 1][j]
                    + P[i][j - 1]
                    - P[i - 1][j - 1]
                    + mat[i - 1][j - 1]
                )

        def getRect(x1, y1, x2, y2):
            return P[x2][y2] - P[x1 - 1][y2] - P[x2][y1 - 1] + P[x1 - 1][y1 - 1]
        
        def can_form_square(size):
            for i in range(1, m - size + 2):
                for j in range(1, n - size + 2):
                    if getRect(i, j, i + size - 1, j + size - 1) <= threshold:
                        return True
            return False


        l, r, ans = 1, min(m, n), 0
        while l <= r:
            mid = (l + r) // 2
            find = can_form_square(mid)
            if find:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans
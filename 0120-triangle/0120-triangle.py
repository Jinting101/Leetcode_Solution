class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i,lst in enumerate(triangle):
            if i == 0:
                continue
            l = len(lst)
            for j,x in enumerate(lst):
                if j == 0:
                    triangle[i][j] += triangle[i-1][0]
                elif j == l-1:
                    triangle[i][j] += triangle[i-1][-1]
                else:
                    triangle[i][j] += min(triangle[i-1][j], triangle[i-1][j-1])
        return min(triangle[-1])


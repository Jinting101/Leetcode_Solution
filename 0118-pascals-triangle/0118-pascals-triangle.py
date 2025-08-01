class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(1, numRows):
            prev = res[-1]
            n = len(prev)
            cur = [1] * (n+1)
            for i in range(1, n):
                cur[i] = prev[i] + prev[i-1]
            res.append(cur)
        return res
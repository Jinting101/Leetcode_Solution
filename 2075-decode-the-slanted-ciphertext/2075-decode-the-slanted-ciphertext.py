class Solution:
    def decodeCiphertext(self, encodedText: str, m: int) -> str:
        n = len(encodedText) // m
        mat = [[" "]*n for _ in range(m)]
        res = ""
        for i,x in enumerate(encodedText):
            mat[i // n][i % n] = x
        for j in range(n):
            col = j
            for i in range(min(m, n-j)):
                res += mat[i][col]
                col += 1
        return res.rstrip()

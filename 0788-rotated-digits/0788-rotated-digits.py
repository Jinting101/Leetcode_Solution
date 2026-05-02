class Solution:
    def rotatedDigits(self, n: int) -> int:
        dif = ['2', '5', '6', '9']
        ndiff = ['3', '4', '7']
        res = 0
        for x in range(1, n+1):
            cnt = sum([1 for digit in str(x) if digit in dif])
            nvcnt = sum([1 for digit in str(x) if digit in ndiff])
            if cnt > 0 and nvcnt == 0:
                res += 1
        return res
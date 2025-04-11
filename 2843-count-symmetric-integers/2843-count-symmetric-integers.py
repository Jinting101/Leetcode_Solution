class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        res = 0
        for x in range(low, high+1):
            y = str(x)
            n = len(y)
            if n % 2 == 1:
                continue
            a, b = y[:n//2], y[n//2:]
            if sum(map(int, a)) == sum(map(int, b)):
                res += 1
        return res
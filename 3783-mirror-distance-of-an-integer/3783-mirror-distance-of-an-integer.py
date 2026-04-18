class Solution:
    def mirrorDistance(self, n: int) -> int:
        revn = 0
        temp = n
        while temp:
            revn = revn * 10 + temp % 10
            temp //= 10
        return abs(n - revn)
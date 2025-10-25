class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n // 7
        left = n % 7
        base = weeks * 28 + (weeks * (weeks-1)) // 2 * 7
        return base + weeks * left + left * (left + 1) // 2
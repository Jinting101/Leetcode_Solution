class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        for x in range(20):
            if 3**x == n:
                return True
        return False

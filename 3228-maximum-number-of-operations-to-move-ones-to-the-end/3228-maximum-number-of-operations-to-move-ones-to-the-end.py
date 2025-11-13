class Solution:
    def maxOperations(self, s: str) -> int:
        res, cur = 0, 0
        added = False
        for x in s[::-1]:
            if x == '1':
                res += cur
                added = False
            else:
                if not added:
                    cur += 1
                    added = not added
        return res
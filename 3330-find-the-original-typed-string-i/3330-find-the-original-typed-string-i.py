class Solution:
    def possibleStringCount(self, word: str) -> int:
        prev, prevcnt = word[0], 0
        res = 1
        for x in word[1:]:
            if x == prev:
                prevcnt += 1
            else:
                res += prevcnt
                prevcnt = 0
                prev = x
        if prevcnt:
            res += prevcnt
        return res
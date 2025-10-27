class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev = 0
        res = 0
        for row in bank:
            cur = sum([int(x) for x in row if x == '1'])
            if cur == 0:
                continue
            if prev:
                res += prev * cur
            prev = cur
        return res
            
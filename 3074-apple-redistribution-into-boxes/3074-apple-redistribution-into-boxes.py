class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        res = 0
        cur, s = 0, sum(apple)
        capacity.sort()
        i = 1
        while cur < s:
            res += 1
            cur += capacity[-i]
            i += 1
        return res

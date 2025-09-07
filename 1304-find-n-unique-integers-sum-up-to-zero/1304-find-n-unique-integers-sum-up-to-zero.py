class Solution:
    def sumZero(self, n: int) -> List[int]:
        l = n if n % 2 == 0 else n-1
        res = []
        cur = 1
        while l > 0:
            res.append(cur)
            if cur > 0:
                cur = -cur
            else:
                cur = 1-cur
            l -= 1
        if n % 2 == 1:
            res.append(0)
        return res
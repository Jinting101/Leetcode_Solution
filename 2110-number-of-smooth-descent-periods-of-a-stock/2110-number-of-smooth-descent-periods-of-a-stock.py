class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)
        res = n
        l = 0
        for r in range(1, n):
            dif = prices[r-1] - prices[r]
            if dif == 1:
                res += r - l
            else:
                l = r
        return res
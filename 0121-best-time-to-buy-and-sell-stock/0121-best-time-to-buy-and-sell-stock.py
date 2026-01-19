class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        min_price = float('inf')
        for x in prices:
            min_price = min(min_price, x)
            res = max(res, x - min_price)
        return res
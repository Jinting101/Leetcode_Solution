class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        cur = prices[0]
        for x in prices[1:]:
            res = max(res, x - cur)
            cur = min(cur, x)
        return res
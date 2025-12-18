class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        res = sum([a*b for a,b in zip(prices, strategy)])
        cur = res
        n = len(prices)
        l, rs = 0, k // 2
        for r in range(k-1, n):
            if l == 0:
                for i in range(rs):
                    cur -= prices[i] * strategy[i]
                for i in range(rs, rs + k // 2):
                    cur += prices[i] * (1 - strategy[i])
            else:
                cur += prices[r] * (1 - strategy[r])
                cur -= prices[rs]
                cur += prices[l-1] * strategy[l-1]
                rs += 1
            res = max(res, cur)
            l += 1
        return res


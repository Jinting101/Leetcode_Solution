class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        cur_min = 0
        cur_max = prices[-1]
        ind = len(prices)-1
        while ind >= 0:
            while ind >= 0 and prices[ind] >= cur_max:
                cur_max = prices[ind]
                ind -= 1
            if ind == -1:
                return res
            if ind == 0:
                return res + cur_max - prices[0]
            cur_min = prices[ind]
            while ind >= 0 and prices[ind] <= cur_min:
                cur_min = prices[ind]
                ind -= 1
            res += cur_max - cur_min
            cur_max = cur_min
        return res
            
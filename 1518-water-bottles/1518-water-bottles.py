class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = emp = numBottles
        while emp >= numExchange:
            numBottles = emp // numExchange
            res += numBottles
            emp = numBottles + emp % numExchange
        return res
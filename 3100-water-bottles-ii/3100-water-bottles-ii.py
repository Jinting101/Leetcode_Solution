class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        res = emp = numBottles
        while emp >= numExchange:
            drink = emp // numExchange
            should_used = numExchange * drink + drink * (drink-1) // 2
            while should_used > emp:
                drink -= 1
                should_used = numExchange * drink + drink * (drink-1) // 2
            emp = emp - should_used + drink
            res += drink
            numExchange += drink
        return res



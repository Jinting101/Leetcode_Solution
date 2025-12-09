class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_eat_up(k):
            if k == 0:
                return False
            return sum([p // k + int(True if p % k else False) for p in piles]) <= h

        l, r = 0, max(piles)
        while l < r:
            mid = (r+l) // 2
            if can_eat_up(mid):
                r = mid
            else:
                l = mid + 1
        return l

        